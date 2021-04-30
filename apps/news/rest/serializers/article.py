from rest_framework import serializers
from apps.abstract.rest.serializers.article import ArticleSerializer
from apps.abstract.rest.serializers.category import CategorySerializer


class NewsSerializer(ArticleSerializer):
    is_pinned = serializers.BooleanField()
    category = CategorySerializer()
