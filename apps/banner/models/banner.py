from django.core.exceptions import ValidationError
from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from .category import Category


class BannerQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publication__lte=now()).exclude(expiration__lte=now())

    def expired(self):
        return self.filter(publication__lt=now(), expiration__lte=now())

    def not_yet(self):
        return self.filter(publication__gt=now())


class Banner(models.Model):
    image = models.ImageField(_("Image"), upload_to="banners/%Y/%m/%d/")
    url = models.URLField(_("URL"))
    name = models.CharField(_("Name"), max_length=150)
    categories = models.ManyToManyField(Category, verbose_name=_("Categories"))
    publication = models.DateTimeField(_("Publication"), default=now)
    expiration = models.DateTimeField(_("Expiration"), null=True, blank=True)

    objects = BannerQuerySet.as_manager()

    class Meta:
        verbose_name = _("Banner")
        verbose_name_plural = _("Banners")
        ordering = ("-publication", )

    def __str__(self):
        return self.name

    def clean(self):
        if self.expired and self.expired <= self.published:
            raise ValidationError({"expired": _("The field must be larger than published")})
