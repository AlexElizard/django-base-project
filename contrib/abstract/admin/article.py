from django.utils.translation import gettext_lazy as _
from .publication import PublicationAdmin


class ArticleAdmin(PublicationAdmin):
    fieldsets = (
        (None, {'fields': ('title', )}),
        (_("Preview"), {'fields': ('preview_image', 'preview_text')}),
        (_("Detail"), {'fields': ('detail_image', 'detail_text')}),
    ) + PublicationAdmin.fieldsets
