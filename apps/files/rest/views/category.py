from rest_framework import generics, permissions
from ..serializers.category import CategorySerializer
from ...models import Category


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.AllowAny, )
