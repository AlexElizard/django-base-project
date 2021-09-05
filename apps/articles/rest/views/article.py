from django_filters import rest_framework as filters
from rest_framework import permissions, viewsets
from ..filters.category import CategoryFilter
from ..serializers.article import ArticleListSerializer, ArticleDetailSerializer
from ...models import Article


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.published()
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = CategoryFilter
    permission_classes = (permissions.AllowAny, )

    def get_serializer_class(self):
        if self.action == 'list':
            return ArticleListSerializer
        elif self.action == 'retrieve':
            return ArticleDetailSerializer
