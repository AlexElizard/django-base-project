from django.db import models
from django.utils.translation import gettext_lazy as _


def _upload_path(instance: 'AbstractFile', filename: str):
    return instance.upload_path(filename)


class AbstractFile(models.Model):
    name = models.CharField(_("Name"), max_length=150)
    file = models.FileField(_("File"), upload_to=_upload_path)
    created = models.DateTimeField(auto_now=True)
    
    def upload_path(self, filename: str):
        """method to provide upload path for file field"""
        raise NotImplementedError()

    class Meta:
        abstract = True
        verbose_name = _("File")
        verbose_name_plural = _("Files")
        ordering = ('-created', )