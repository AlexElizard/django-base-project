from rest_framework import serializers
from ..category.serializers import CategorySerializer


class CKEditorTextField(serializers.CharField):
    def to_representation(self, value):
        base_uri = self.context['request'].build_absolute_uri('/')
        return value.replace('src="/', f'src="{base_uri}')


class PageListSerializer(serializers.Serializer):
    slug = serializers.IntegerField(source='id')
    title = serializers.CharField()
    category = CategorySerializer()


class PageRetrieveSerializer(serializers.Serializer):
    title = serializers.CharField()
    text = CKEditorTextField()
