from django.contrib import admin


class BaseCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
