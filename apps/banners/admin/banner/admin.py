from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .filters import PublishFilterAdmin
from ...models import Banner


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('image', 'name', 'url', 'categories')}),
        (_("Publication"), {'fields': ('publication', 'expiration')}),
    )
    filter_horizontal = ('categories', )
    list_filter = ('categories', PublishFilterAdmin)
    list_display = ('name', 'url', 'publication', 'expiration')
