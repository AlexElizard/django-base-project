from django.contrib import admin
from .models import Category, Banner


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    filter_horizontal = ('categories', )
    list_display = ('name', 'url', 'published', 'expired')
    list_filter = ('categories', )
