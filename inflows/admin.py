from django.contrib import admin
from .models import Inflow


@admin.register(Inflow)
class InflowAdmin(admin.ModelAdmin):

    list_display = [
        'suplier',
        'product',
        'description',
    ]
    search_fields = [
        'suplier',
        'product',
    ]
    list_filter = [
        'suplier',
        'product',
        'description',
    ]
    fields = [
        'suplier',
        'product',
        'description',
    ]
