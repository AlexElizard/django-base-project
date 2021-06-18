from django_filters import rest_framework as filters
from rest_framework import viewsets, permissions
from .filters import CategoryFilter
from .serializers import PageListSerializer, PageRetrieveSerializer
from ...models import Page


class PageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Page.objects.all()
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = CategoryFilter
    permission_classes = (permissions.AllowAny, )

    def get_serializer_class(self):
        if self.action == 'list':
            return PageListSerializer
        elif self.action == 'retrieve':
            return PageRetrieveSerializer
