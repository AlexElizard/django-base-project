from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .filter import PublishFilterAdmin
from ..models import Article, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('is_pinned', 'title', 'category')}),
        (_("Preview"), {'fields': ('preview_image', 'preview_text')}),
        (_("Detail"), {'fields': ('detail_image', 'detail_text')}),
        (_("Publication"), {'fields': ('published', 'expired')}),
    )
    list_filter = ('category', PublishFilterAdmin)
