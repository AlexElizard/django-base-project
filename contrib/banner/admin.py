from contrib.abstract.admin.publication import PublicationAdmin
from contrib.abstract.admin.category import BaseCategoryAdmin
from django.contrib import admin
from .models import Category, Banner


class BaseBannerAdmin(PublicationAdmin):
    fieldsets = ((None, {'fields': ('image', 'name', 'url')}), ) + PublicationAdmin.fieldsets
    list_display = ('name', 'url', 'published', 'expired')


@admin.register(Category)
class CategoryAdmin(BaseCategoryAdmin):
    pass


@admin.register(Banner)
class BannerAdmin(BaseBannerAdmin):
    fieldsets = ((None, {'fields': ('image', 'name', 'url', 'categories')}), ) + BaseBannerAdmin.fieldsets[1:]
    filter_horizontal = ('categories', )
    list_filter = ('categories', ) + BaseBannerAdmin.list_filter
