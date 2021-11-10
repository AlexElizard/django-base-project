from django.contrib.admin import TabularInline


class ModelNameInline(TabularInline):
    model = None
    fields = ("", )
    extra = 0
    ordering = ("", )
