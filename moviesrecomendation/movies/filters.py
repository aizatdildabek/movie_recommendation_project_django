from django_filters import rest_framework as filters
from movies.models import Movie


def icontains_distinct(queryset, name, value):
    lookup = f"{name}__icontains" 
    # return queryset.filter(**{lookup: value})
    return queryset.filter(ratings__icontains=value)

class MovieFilter(filters.FilterSet):
    # title = filters.CharFilter(field_name = 'title', lookup_expr='icontains')
    # release_year = filters.NumberFilter()

    class Meta:
        model = Movie
        fields = {
            'title':['exact', 'contains', 'icontains'],
            'release_year':['exact', 'gte', 'lte'],
            'producer':['exact'],
            }

    def filter_queryset(self, queryset):
        queryset = super().filter_queryset(queryset)
        return queryset.distinct()

    # def qs(self):
    #     pass