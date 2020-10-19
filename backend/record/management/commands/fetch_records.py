import os
from datetime import datetime
from timeit import default_timer as timer

import pytz
import requests
from celery import task
from django.core.management.base import BaseCommand

from market.models import Market
from record.models import Record


@task()
def fetch_records():
    url = os.environ.get('MARKETS_URL', 'http://api.bitcoincharts.com/v1/markets.json')
    response = requests.get(url)
    records = response.json()
    counter = 0
    for record in records:
        market = Market.objects.get(symbol=record['symbol'])

        # Perform conversions in order to get time zone aware object
        latest_trade = datetime.utcfromtimestamp(record['latest_trade'])
        latest_trade = pytz.timezone('UTC').localize(latest_trade)

        # Add new market record if it has been updated
        if not Record.objects.filter(market=market, latest_trade=latest_trade).exists():
            # Set all previous records last_record field to False since
            # new one is being recorded
            Record.objects.filter(market=market).update(last_record=False)
            # Add new record to the database
            Record.objects.create(market=market,
                                  bid=record['bid'],
                                  ask=record['ask'],
                                  latest_trade=latest_trade,
                                  high=record['high'],
                                  low=record['low'],
                                  close=record['close'],
                                  volume=record['volume'],
                                  currency_volume=record['currency_volume'],
                                  weighted_price=record['weighted_price'],
                                  duration=record['duration'],
                                  avg=record['avg'])

            counter += 1

    return counter


class Command(BaseCommand):
    help = 'Populate database with latest market records'

    def handle(self, *args, **options):
        start = timer()
        new_records = fetch_records()
        end = timer()

        elapsed_time = end - start
        second_plural = 'second' if str(elapsed_time)[-1] == '1' else 'seconds'
        record_plural = 'record' if str(new_records)[-1] == '1' else 'records'
        self.stdout.write(self.style.SUCCESS(
            ('It took {0} ' + second_plural + ' to fetch {1} ' + record_plural + '.')
                .format(round(elapsed_time, 3), new_records)))
