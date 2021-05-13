from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views.category import CategoryListAPIView
from .views.page import PageViewSet

router = SimpleRouter()
router.register('', PageViewSet)

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view()),
    path('', include(router.urls)),
]
