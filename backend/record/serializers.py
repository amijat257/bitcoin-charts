from rest_framework import serializers

from market.serializers import MarketSerializer
from .models import Record


class RecordSerializer(serializers.ModelSerializer):
    market = MarketSerializer()

    class Meta:
        model = Record
        fields = '__all__'
