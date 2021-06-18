from django.contrib import admin
from ...models import Page


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('title', 'category', 'text',)}),
    )
    list_filter = ('category',)
    list_display = ('title', 'category')
