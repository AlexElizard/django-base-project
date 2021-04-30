from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from apps.abstract.models.article import AbstractBaseArticle
from .category import Category


class Article(AbstractBaseArticle):
    is_pinned = models.BooleanField(_("Pinned"))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_("Category"))

    def preview_upload_path(self: 'AbstractBaseArticle', filename: str):
        date = now().date()
        return f'news/{date.year}/{date.month}/{date.day}/news_{self.pk}_preview_{filename}'

    def detail_upload_path(self: 'AbstractBaseArticle', filename: str):
        date = now().date()
        return f'news/{date.year}/{date.month}/{date.day}/news_{self.pk}_detail_{filename}'
