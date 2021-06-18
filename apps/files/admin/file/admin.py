from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .filters import PublishFilterAdmin
from ...models import File


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('name', 'file', 'category')}),
        (_("Publication"), {'fields': ('publication', 'expiration')}),
    )
    filter_horizontal = ('companies', )
    list_filter = ('category', 'companies', PublishFilterAdmin)
    list_display = ('name', 'category', 'publication', 'expiration')
