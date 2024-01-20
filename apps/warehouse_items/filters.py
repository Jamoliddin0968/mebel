from django_filters import rest_framework as filters

from .models import WareHouseItem


class WareHouseItemFilter(filters.FilterSet):
    warehouse_id = filters.NumberFilter()
    category_id = filters.NumberFilter(method='filter_by_category')

    def filter_by_category(self, queryset, name, value):
        return queryset.filter(product__category__id=value)

    class Meta:
        model = WareHouseItem
        fields = ['warehouse_id', 'category_id']
