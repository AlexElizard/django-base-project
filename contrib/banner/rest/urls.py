from django.urls import path
from .views.category import CategoryListAPIView
from .views.banner import BannerListAPIView


urlpatterns = [
    path('', BannerListAPIView.as_view()),
    path('categories/', CategoryListAPIView.as_view()),
]
