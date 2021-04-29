from django.utils.timezone import now
from django_filters import rest_framework as filters
from rest_framework import generics, permissions
from ..filters.banner import BannerFilter
from ..serializers.banners import BannerSerializer
from ...models import Banner


class BannerListAPIView(generics.ListAPIView):
    queryset = Banner.objects.active()
    serializer_class = BannerSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = BannerFilter
    permission_classes = (permissions.AllowAny, )
