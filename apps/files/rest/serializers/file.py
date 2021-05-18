from rest_framework import serializers
from .category import CategorySerializer


class FileSerializer(serializers.Serializer):
    name = serializers.CharField()
    file = serializers.FileField()
    category = CategorySerializer()
    publication = serializers.DateTimeField()
