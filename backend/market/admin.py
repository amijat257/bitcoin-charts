from django.contrib import admin

from .models import Market


class MarketAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'symbol', 'currency', 'website', 'active')
    search_fields = ("name", "symbol", 'website')


admin.site.register(Market, MarketAdmin)
