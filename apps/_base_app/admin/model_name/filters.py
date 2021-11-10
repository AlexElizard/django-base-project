from django.contrib.admin import SimpleListFilter
from django.utils.translation import gettext_lazy as _


class ModelNameFilter(SimpleListFilter):
    title = _("")
    parameter_name = "param_name"

    def lookups(self, request, model_admin):
        return (
            ("param_value", _("ParamValueName")),
        )

    def queryset(self, request, queryset):
        return queryset
