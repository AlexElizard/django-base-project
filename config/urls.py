from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns.append(path('__debug__/', include(debug_toolbar.urls)))

    if 'drf_spectacular' in settings.INSTALLED_APPS:
        from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

        urlpatterns.append(
            path('swagger/', include([
                path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
                path('schema/', SpectacularAPIView.as_view(), name='schema')
            ]))
        )