from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.translation import gettext_lazy as _
from .category import Category


class Page(models.Model):
    title = models.CharField(_("Title"), max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_("Category"))
    text = RichTextUploadingField(_("Text"))

    class Meta:
        verbose_name = _("Page")
        verbose_name_plural = _("Pages")
        ordering = ("category", "title")

    def __str__(self):
        return self.title
