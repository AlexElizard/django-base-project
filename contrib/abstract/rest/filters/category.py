from django_filters import rest_framework as filters


class CategoryFilter(filters.FilterSet):
    categories = filters.CharFilter(field_name="categories__slug")
