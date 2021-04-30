from django.db import models
from django.utils.translation import gettext_lazy as _
from contrib.abstract.models.publication import AbstractPublication
from .category import Category


class AbstractBaseBanner(AbstractPublication):
    image = models.ImageField(_("Image"), upload_to='banners/images/%Y/%m/%d/')
    url = models.URLField(_("URL"))
    name = models.CharField(_("Name"), max_length=150)

    class Meta(AbstractPublication.Meta):
        abstract = True
        verbose_name = _("Banner")
        verbose_name_plural = _("Banners")

    def __str__(self):
        return self.name


class Banner(AbstractBaseBanner):
    categories = models.ManyToManyField(Category, verbose_name=_("Categories"))
