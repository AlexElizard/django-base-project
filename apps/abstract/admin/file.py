from django.contrib import admin


class FileInline(admin.TabularInline):
    model = None
    extra = 1
