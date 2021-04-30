from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.abstract.models.publication import AbstractPublication


def _preview_upload_path(instance, filename: str):
    return instance.preview_upload_path(filename)


def _detail_upload_path(instance, filename: str):
    return instance.detail_upload_path(filename)


class AbstractBaseArticle(AbstractPublication):
    title = models.CharField(_("Title"), max_length=150)
    preview_image = models.ImageField(_("Preview image"), upload_to=_preview_upload_path)
    preview_text = RichTextUploadingField(_("Preview text"))
    detail_image = models.ImageField(_("Detail image"), upload_to=_detail_upload_path)
    detail_text = RichTextUploadingField(_("Detail text"))

    class Meta(AbstractPublication.Meta):
        abstract = True
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")

    def __str__(self):
        return self.title

    def preview_upload_path(self, filename: str):
        """method to provide upload path for preview_image field"""
        raise NotImplementedError()

    def detail_upload_path(self, filename: str):
        """method to provide upload path for detail_image field"""
        raise NotImplementedError()
