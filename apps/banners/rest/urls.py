from django.urls import path
from .views.banner import BannerListAPIView
from .views.category import CategoryListAPIView


urlpatterns = [
    path('', BannerListAPIView.as_view()),
    path('categories/', CategoryListAPIView.as_view()),
]
