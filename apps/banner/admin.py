from django.contrib import admin
from apps.abstract.admin.category import BaseCategoryAdmin
from apps.abstract.admin.publication import PublicationAdmin
from .models import Category, Banner


@admin.register(Category)
class CategoryAdmin(BaseCategoryAdmin):
    pass


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    fieldsets = ((None, {'fields': ('image', 'name', 'url', 'categories')}), ) + PublicationAdmin.fieldsets[:]
    filter_horizontal = ('categories', )
    list_filter = ('categories', ) + PublicationAdmin.list_filter
    list_display = ('name', 'url', 'published', 'expired')
