from rest_framework import generics, filters
from ..serializers.file import FileSerializer


class BaseFileListAPIView(generics.ListAPIView):
    queryset = None
    serializer_class = FileSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', )