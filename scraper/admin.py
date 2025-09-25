from django.contrib import admin
from .models import KhorasanRate
from .models import SaraiRate
from .models import DaAfgRate

@admin.register(KhorasanRate)
class KhorasanRateAdmin(admin.ModelAdmin):
    list_display = ('currency', 'buying_rate', 'selling_rate', 'up', 'down', 'updated_time','timestamp')
    list_filter = ('currency','up', 'down', 'timestamp')
    ordering = ('-timestamp',)
    search_fields = ('currency',)
        


@admin.register(SaraiRate)
class SaraiRateAdmin(admin.ModelAdmin):
    list_display = ('currency', 'buying_rate', 'selling_rate', 'up', 'down', 'updated_time','timestamp')
    list_filter = ('currency','up', 'down', 'timestamp')
    ordering = ('-timestamp',)
    search_fields = ('currency',)



@admin.register(DaAfgRate)
class DaAfgRateAdmin(admin.ModelAdmin):
    list_display = ('currency', 'buying_rate', 'selling_rate', 'up', 'down', 'updated_time','timestamp')
    list_filter = ('currency','up', 'down', 'timestamp')
    ordering = ('-timestamp',)
    search_fields = ('currency',)