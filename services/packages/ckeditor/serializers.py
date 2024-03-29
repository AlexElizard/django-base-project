from rest_framework import serializers


class CKEditorTextField(serializers.CharField):
    """Поле, которое заменяет относительный url-файлов на абсолютный"""
    def to_representation(self, value):
        base_uri = self.context['request'].build_absolute_uri('/')
        return value.replace('src="/', f'src="{base_uri}')
