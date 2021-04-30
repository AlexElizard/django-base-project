from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views.article import ArticleViewSet
from .views.category import CategoryListAPIView

router = SimpleRouter()
router.register('', ArticleViewSet)

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view()),
    path('', include(router.urls)),
]
