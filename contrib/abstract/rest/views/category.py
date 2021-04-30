from rest_framework import generics, permissions
from contrib.abstract.rest.serializers.category import CategorySerializer


class BaseCategoryListAPIView(generics.ListAPIView):
    queryset = None
    serializer_class = CategorySerializer
    permission_classes = (permissions.AllowAny, )
