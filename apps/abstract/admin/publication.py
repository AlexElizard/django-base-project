from django.contrib import admin
from django.utils.timezone import now
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
            qs = qs.filter(published__lte=now(), expired__lte=now())
        elif self.value() == 'published':
            qs = qs.filter(published__lte=now()).exclude(expired__lte=now())
        elif self.value() == 'not_yet':
            qs = qs.filter(published__gt=now(), expired__gt=now())
        return qs


class PublicationAdmin(admin.ModelAdmin):
    fieldsets = (
        (_("Publication"), {'fields': ('published', 'expired')}),
    )
    list_filter = (PublishFilterAdmin, )
