from django_filters import rest_framework as filters
from apps.abstract.rest.filters.category import CategoryFilter
from apps.abstract.rest.views.article import BaseArticleViewSet
from ..serializers.article import NewsSerializer
from ...models import Article


class ArticleViewSet(BaseArticleViewSet):
    queryset = Article.objects.published()
    serializer_class = NewsSerializer
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = CategoryFilter
