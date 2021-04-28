from django_filters import rest_framework as filters


class BannerFilter(filters.FilterSet):
    categories = filters.CharFilter(field_name="categories__slug")
