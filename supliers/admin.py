from django.contrib import admin
from .models import Suplier


@admin.register(Suplier)
class SuplierAdmin(admin.ModelAdmin):

    fields = ['name', 'description',]
    search_fields = ['name',]
    list_filter = ['active',]
    readonly_fields = ['uuid', 'created_at', 'modified_at', 'created_by']
