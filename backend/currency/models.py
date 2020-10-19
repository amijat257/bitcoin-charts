from django.db import models


class Currency(models.Model):
    name = models.CharField(max_length=50)

    code = models.CharField(max_length=10, unique=True)

    symbol = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name_plural = 'Currencies'
