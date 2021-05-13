from rest_framework import serializers
from .category import CategorySerializer


class CKEditorTextField(serializers.CharField):
    def to_representation(self, value):
        base_uri = self.context['request'].build_absolute_uri('/')
        return value.replace('src="/', f'src="{base_uri}')


class ArticleListSerializer(serializers.Serializer):
    is_pinned = serializers.BooleanField()
    title = serializers.CharField()
    category = CategorySerializer()
    preview_image = serializers.ImageField()
    preview_text = CKEditorTextField
    published = serializers.DateTimeField()


class ArticleDetailSerializer(serializers.Serializer):
    title = serializers.CharField()
    category = CategorySerializer()
    detail_image = serializers.ImageField()
    detail_text = CKEditorTextField
    published = serializers.DateTimeField()
