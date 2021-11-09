from rest_framework import serializers


class ChildrenSerializerMixin(serializers.Serializer):
    """Миксин для вывода дерева"""
    children = serializers.SerializerMethodField()

    def get_children(self, obj):
        serializer = self.__class__(obj.get_children(), many=True, context=self.context)
        return serializer.data
