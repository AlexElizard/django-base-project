from rest_framework import serializers


class FileSerializer(serializers.Serializer):
    name = serializers.CharField()
    file = serializers.FileField()
    created = serializers.DateTimeField()
