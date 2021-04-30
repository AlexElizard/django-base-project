from contrib.abstract.models.article import AbstractBaseArticle
from django.db import models
from django.utils.translation import gettext_lazy as _
from .category import Category


class Article(AbstractBaseArticle):
    is_pinned = models.BooleanField(_("Pinned"))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_("Category"))
