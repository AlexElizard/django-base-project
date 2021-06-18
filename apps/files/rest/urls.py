from django.urls import path
from .category.views import CategoryListAPIView
from .file.views import FileListAPIView


urlpatterns = [
    path('', FileListAPIView.as_view()),
    path('categories/', CategoryListAPIView.as_view()),
]
