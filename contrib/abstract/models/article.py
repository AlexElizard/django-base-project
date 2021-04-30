from ckeditor_uploader.fields import RichTextUploadingField
from contrib.abstract.models.publication import AbstractPublication
from django.db import models
from django.utils.translation import gettext_lazy as _


class AbstractBaseArticle(AbstractPublication):
    title = models.CharField(_("Title"), max_length=150)
    preview_image = models.ImageField(_("Preview image"))
    preview_text = RichTextUploadingField(_("Preview text"))
    detail_image = models.ImageField(_("Detail image"))
    detail_text = RichTextUploadingField(_("Detail text"))

    class Meta(AbstractPublication.Meta):
        abstract = True
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")

    def __str__(self):
        return self.title
