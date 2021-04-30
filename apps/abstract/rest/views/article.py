from rest_framework import permissions, viewsets
from apps.abstract.rest.serializers.article import ArticleSerializer


class BaseArticleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = None
    serializer_class = ArticleSerializer
    permission_classes = (permissions.AllowAny)
