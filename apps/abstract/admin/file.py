from django.contrib import admin


class AbstractFileInline(admin.TabularInline):
    model = None
    extra = 1
