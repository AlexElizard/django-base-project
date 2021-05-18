from django.core.exceptions import ValidationError
from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from .category import Category


class FileQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publication__lte=now()).exclude(expiration__lte=now())

    def expired(self):
        return self.filter(publication__lt=now(), expiration__lte=now())

    def not_yet(self):
        return self.filter(publication__gt=now())


class File(models.Model):
    name = models.CharField(_("Name"), max_length=255)
    file = models.FileField(_("File"), upload_to='files/%Y/%m/%d/')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name=_("Category"))
    publication = models.DateTimeField(_("Publication"), default=now)
    expiration = models.DateTimeField(_("Expiration"), blank=True, null=True)

    objects = FileQuerySet.as_manager()

    def clean(self):
        if self.expiration and self.expiration <= self.publication:
            raise ValidationError({"expired": _("The field must be larger than published")})

    class Meta:
        verbose_name = _("File")
        verbose_name_plural = _("Files")

    def __str__(self):
        return self.name
