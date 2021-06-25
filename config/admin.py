from django.contrib.admin import *


class CustomAdminSite(AdminSite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._registry.update(site._registry)
        for model, model_admin in self._registry.items():
            model_admin.admin_site = self


site = CustomAdminSite()
