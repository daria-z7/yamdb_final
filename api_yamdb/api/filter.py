from django_filters import CharFilter, FilterSet
from reviews.models import Title


class TitleFilterSet(FilterSet):
    category = CharFilter(field_name='category__slug')
    genre = CharFilter(field_name='genre__slug')
    name = CharFilter(lookup_expr='icontains')

    class Meta:
        model = Title
        fields = ('category', 'genre', 'year', 'name')
