from django.contrib import admin
from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ['name', 'description',]
    fields = ['name', 'description',]
    list_filter = ['active',]
    search_fields = ['name',]
    readonly_fields = ['uuid', 'created_at', 'modified_at', 'created_by']
