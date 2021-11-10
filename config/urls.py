from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/admin-panel/', include([

    ])),
    path('api/', include([

    ])),
]

if 'ckeditor_uploader' in settings.INSTALLED_APPS:
    urlpatterns.append(path('api/ckeditor/', include('ckeditor_uploader.urls')))

if 'drf_spectacular' in settings.INSTALLED_APPS:
    from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
    urlpatterns.append(
        path('swagger/', include([
            path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
            path('schema/', SpectacularAPIView.as_view(), name='schema')
        ]))
    )

if 'rest_framework_simplejwt.authentication.JWTAuthentication' in settings.REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES']:
    from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
    urlpatterns.append(path('api/auth/token/', include([
        path('', TokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
        path('verify/', TokenVerifyView.as_view(), name='token_verify'),
    ])))

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns.append(path('__debug__/', include(debug_toolbar.urls)))
