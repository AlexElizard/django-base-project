from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .category.views import CategoryListAPIView
from .page.views import PageViewSet

router = SimpleRouter()
router.register('', PageViewSet)

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view()),
    path('', include(router.urls)),
]
