from django_filters import rest_framework as filters
from rest_framework import permissions, viewsets
from rest_framework.pagination import LimitOffsetPagination
from ..filters.category import CategoryFilter
from ..serializers.article import ArticleListSerializer, ArticleDetailSerializer
from ...models import Article


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.published()
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = CategoryFilter
    pagination_class = LimitOffsetPagination
    permission_classes = (permissions.AllowAny, )

    def get_serializer_class(self):
        if self.action == 'list':
            return ArticleListSerializer
        elif self.action == 'retrieve':
            return ArticleDetailSerializer
