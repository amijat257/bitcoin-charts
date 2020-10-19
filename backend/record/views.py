from rest_framework.generics import ListAPIView

from .models import Record
from .serializers import RecordSerializer


class TopRecordsView(ListAPIView):
    """
    Get records of Top 20 markets by volume
    """
    serializer_class = RecordSerializer

    def get_queryset(self):
        return Record.objects.get_top_20_by_volume()
