import django_filters
from .models import Fish


class FishFilter(django_filters.FilterSet):
    price = django_filters.RangeFilter()
    
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Fish
        fields = ['price', 'name']