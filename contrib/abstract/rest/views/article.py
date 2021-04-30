from django_filters import rest_framework as filters
from rest_framework import permissions, viewsets
from contrib.abstract.rest.filters.category import CategoryFilter
from contrib.abstract.rest.serializers.article import ArticleSerializer


class BaseArticleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = None
    serializer_class = ArticleSerializer
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = CategoryFilter
    permission_classes = (permissions.AllowAny)
