from ckeditor_uploader.fields import RichTextUploadingField
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from .category import Category


class ArticleQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publication__lte=now()).exclude(expiration__lte=now())

    def expired(self):
        return self.filter(publication__lt=now(), expiration__lte=now())

    def not_yet(self):
        return self.filter(publication__gt=now())


class Article(models.Model):
    is_pinned = models.BooleanField(_("Pinned"))
    title = models.CharField(_("Title"), max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_("Category"))
    preview_image = models.ImageField(_("Preview image"), upload_to="articles/%Y/%m/%d/preview/")
    preview_text = RichTextUploadingField(_("Preview text"))
    detail_image = models.ImageField(_("Detail image"), upload_to="articles/%Y/%m/%d/detail/")
    detail_text = RichTextUploadingField(_("Detail text"))
    publication = models.DateTimeField(_("Publication"), default=now)
    expiration = models.DateTimeField(_("Expiration"), null=True, blank=True)

    objects = ArticleQuerySet.as_manager()

    def clean(self):
        if self.expiration and self.expiration <= self.publication:
            raise ValidationError({"expired": _("The field must be larger than published")})

    class Meta:
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")
        ordering = ('-is_pinned', '-publication')
