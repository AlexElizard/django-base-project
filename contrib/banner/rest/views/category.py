from rest_framework import generics
from ..serializers.category import CategorySerializer
from ...models import Category


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
