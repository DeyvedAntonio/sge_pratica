from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    fields = ['name', 'description',]
    search_fields = ['name',]
    list_filter = ['active',]
    readonly_fields = ['uuid', 'created_at', 'modified_at', 'created_by']
