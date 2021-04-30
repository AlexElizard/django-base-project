from contrib.abstract.rest.views.category import BaseCategoryListAPIView
from ...models import Category


class CategoryListAPIView(BaseCategoryListAPIView):
    queryset = Category.objects.all()
