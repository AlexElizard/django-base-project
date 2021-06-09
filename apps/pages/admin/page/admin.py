from django.contrib import admin
from ..models import Category, Page


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('title', 'category', 'text',)}),
    )
    list_filter = ('category',)
    list_display = ('title', 'category')
