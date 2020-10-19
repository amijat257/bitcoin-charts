from django.db import models


class RecordManager(models.Manager):
    def get_top_20_by_volume(self):
        return self.filter(last_record=True).order_by('-volume')[:20]
