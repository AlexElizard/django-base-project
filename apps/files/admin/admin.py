from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .filters import PublishFilterAdmin
from ..models import Category, File


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('name', 'file', 'category')}),
        (_("Publication"), {'fields': ('publication', 'expiration')}),
    )
    list_filter = ('category', PublishFilterAdmin)
    list_display = ('name', 'category', 'publication', 'expiration')
