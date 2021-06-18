from django_filters import rest_framework as filters


class CategoryFilter(filters.FilterSet):
    category = filters.CharFilter(field_name="category__slug")
