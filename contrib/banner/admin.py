from django.contrib import admin
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from .models import Category, Banner


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


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    filter_horizontal = ('categories', )
    list_display = ('name', 'url', 'published', 'expired')
    list_filter = ('categories', )
