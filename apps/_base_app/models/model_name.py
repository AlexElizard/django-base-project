from django.db import models
from django.utils.translation import gettext_lazy as _


class ModelNameQuerySet(models.QuerySet):
    pass


class ModelName(models.Model):

    objects = ModelNameQuerySet.as_manager()

    def clean(self):
        pass

    def __str__(self):
        return ""

    class Meta:
        ordering = ("", )
        verbose_name = _("ModelName")
        verbose_name_plural = _("ModelsNames")
