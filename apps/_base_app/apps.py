from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BaseAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps._base_app'
    verbose_name = _("BaseApp")
