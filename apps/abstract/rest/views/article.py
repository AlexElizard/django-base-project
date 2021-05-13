from rest_framework import permissions, viewsets
from rest_framework.pagination import LimitOffsetPagination
from apps.abstract.rest.serializers.article import ArticleSerializer


class BaseArticleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = None
    serializer_class = ArticleSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (permissions.AllowAny, )
