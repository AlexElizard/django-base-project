from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from apps.abstract.models.publication import AbstractPublication
from .category import Category


def _image_upload_path(instance: 'Banner', filename: str):
    date = now().date()
    return f'banners/{date.year}/{date.month}/{date.day}/banner_{instance.pk}_{filename}'


class Banner(AbstractPublication):
    image = models.ImageField(_("Image"), upload_to=_image_upload_path)
    url = models.URLField(_("URL"))
    name = models.CharField(_("Name"), max_length=150)
    categories = models.ManyToManyField(Category, verbose_name=_("Categories"))

    class Meta(AbstractPublication.Meta):
        verbose_name = _("Banner")
        verbose_name_plural = _("Banners")

    def __str__(self):
        return self.name
