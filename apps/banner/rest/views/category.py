from rest_framework import generics, permissions
from apps.abstract.rest.serializers.category import CategorySerializer
from ...models import Category


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.AllowAny, )
