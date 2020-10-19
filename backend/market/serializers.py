from rest_framework import serializers

from currency.serializers import CurrencySerializer
from .models import Market


class MarketSerializer(serializers.ModelSerializer):
    currency = CurrencySerializer()

    class Meta:
        model = Market
        fields = '__all__'
