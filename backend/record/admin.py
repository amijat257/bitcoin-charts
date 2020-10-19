from django.contrib import admin
from .models import Record


class RecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'market', 'weighted_price', 'volume', 'latest_trade', 'last_record')
    search_fields = ("market__name", "market__symbol", 'market__website')
    list_filter = ('last_record',)


admin.site.register(Record, RecordAdmin)
