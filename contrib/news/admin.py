from django.contrib import admin
from contrib.abstract.admin.article import ArticleAdmin as BaseArticleAdmin
from .models import Article, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Article)
class ArticleAdmin(BaseArticleAdmin):
    fieldsets = ((None, {'fields': ('title', 'category')}), ) + BaseArticleAdmin.fieldsets[1:]
    list_filter = ('category',) + BaseArticleAdmin.list_filter
