from django.db import models


class Market(models.Model):
    name = models.CharField(max_length=50)

    symbol = models.CharField(max_length=20)

    currency = models.ForeignKey('currency.Currency',
                                 on_delete=models.CASCADE,
                                 related_name='currency_market')

    website = models.URLField(blank=True)

    active = models.BooleanField(default=False)

    def __str__(self):
        return self.symbol
