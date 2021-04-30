from rest_framework import serializers
from contrib.abstract.rest.serializers.article import ArticleSerializer
from contrib.abstract.rest.serializers.category import CategorySerializer


class NewsSerializer(ArticleSerializer):
    is_pinned = serializers.BooleanField()
    category = CategorySerializer()
