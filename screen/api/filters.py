import django_filters
from screen.models import Movie

class MovieFilter(django_filters.FilterSet):
    year=django_filters.CharFilter(field_name='year',lookup_expr='iexact')
    class Meta:
        model = Movie
        fields=['year']