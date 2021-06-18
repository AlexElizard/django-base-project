from rest_framework import generics, permissions
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .filters import CategoryFilter
from .serializers import FileSerializer
from ...models import File


class FileListAPIView(generics.ListAPIView):
    """Возвращает список регламентов"""
    queryset = File.objects.published()
    serializer_class = FileSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filterset_class = CategoryFilter
    search_fields = ('name', )
    permission_classes = (permissions.AllowAny, )
