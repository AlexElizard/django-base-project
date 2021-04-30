from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _


class PublicationQuerySet(models.QuerySet):
    def published(self):
        return self.filter(published__lte=now()).exclude(expired__lte=now())

    def expired(self):
        return self.filter(published__lte=now(), expired__lte=now())


class AbstractPublication(models.Model):
    published = models.DateTimeField(_("Published"), default=now)
    expired = models.DateTimeField(_("Expired"), null=True, blank=True)

    objects = PublicationQuerySet.as_manager()

    class Meta:
        abstract = True
        ordering = ("-published", "-expired")
