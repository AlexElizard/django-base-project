from rest_framework import serializers
from ..category.serializers import CategorySerializer


class FileSerializer(serializers.Serializer):
    name = serializers.CharField()
    file = serializers.FileField()
    category = CategorySerializer()
    created = serializers.DateTimeField(source='publication')
