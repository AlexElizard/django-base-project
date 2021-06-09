from django.urls import path
from .banner.views import BannerListAPIView
from .category.views import CategoryListAPIView


urlpatterns = [
    path('', BannerListAPIView.as_view()),
    path('categories/', CategoryListAPIView.as_view()),
]
