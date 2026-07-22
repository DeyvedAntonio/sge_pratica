from django.contrib import admin
from .models import Brand


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):

    fields = ['name', 'description',]
    search_fields = ['name',]
