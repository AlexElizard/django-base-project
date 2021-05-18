from django.urls import path
from .views.category import CategoryListAPIView
from .views.file import FileListAPIView


urlpatterns = [
    path('', FileListAPIView.as_view()),
    path('categories/', CategoryListAPIView.as_view()),
]
