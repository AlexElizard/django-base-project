from rest_framework import serializers
from . import CKEditorTextField


class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField()
    preview_image = serializers.ImageField()
    preview_text = CKEditorTextField
    detail_image = serializers.ImageField()
    detail_text = CKEditorTextField
    published = serializers.DateTimeField()
