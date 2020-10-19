from django.db import models
from .managers import RecordManager


class Record(models.Model):
    market = models.ForeignKey('market.Market',
                               on_delete=models.CASCADE,
                               related_name='record_market')

    bid = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True, default=None)

    ask = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True, default=None)

    latest_trade = models.DateTimeField()

    high = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True, default=None)

    low = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True, default=None)

    close = models.DecimalField(max_digits=18, decimal_places=3)

    volume = models.DecimalField(max_digits=18, decimal_places=3)

    currency_volume = models.DecimalField(max_digits=18, decimal_places=3)

    weighted_price = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True, default=None)

    duration = models.PositiveIntegerField()

    avg = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True, default=None)

    created_at = models.DateTimeField(auto_now_add=True)

    last_record = models.BooleanField(default=True)

    objects = RecordManager()

    def __str__(self):
        return self.market.name
