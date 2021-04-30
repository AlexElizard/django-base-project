from django_filters import rest_framework as filters
from rest_framework import permissions, viewsets
from contrib.abstract.rest.filters.category import CategoryFilter
from ..serializers.article import NewsSerializer
from ...models import Article


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.published()
    serializer_class = NewsSerializer
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = CategoryFilter
    permission_classes = (permissions.AllowAny)
