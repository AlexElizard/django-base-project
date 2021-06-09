from django_filters import rest_framework as filters
from rest_framework import generics, permissions
from .filters import CategoryFilter
from .serializers import BannerSerializer
from ...models import Banner


class BannerListAPIView(generics.ListAPIView):
    queryset = Banner.objects.published()
    serializer_class = BannerSerializer
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = CategoryFilter
    permission_classes = (permissions.AllowAny, )
