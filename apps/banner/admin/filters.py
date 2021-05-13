from django.contrib import admin
from django.utils.translation import gettext_lazy as _


class PublishFilterAdmin(admin.SimpleListFilter):
    title = _("Publication status")
    parameter_name = 'pub_status'

    def lookups(self, request, model_admin):
        return (
            ("expired", _("Expired")),
            ("published", _("Published")),
            ("not_yet", _("Not yet published")),
        )

    def queryset(self, request, queryset):
        qs = queryset
        if self.value() == 'expired':
            qs = qs.expired()
        elif self.value() == 'published':
            qs = qs.published()
        elif self.value() == 'not_yet':
            qs = qs.not_yet()
        return qs
