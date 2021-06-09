from rest_framework import serializers


class BannerSerializer(serializers.Serializer):
    image = serializers.ImageField()
    name = serializers.CharField()
    url = serializers.URLField()
