from django.db.models import Q
from django_filters import NumberFilter
from django_filters.rest_framework import FilterSet

from goods.models import Goods





class GoodsFilter(FilterSet):
    pricemin = NumberFilter(field_name="shop_price", help_text="最低价格", lookup_expr="gte")
    pricemax = NumberFilter(field_name='shop_price', lookup_expr='lte')
    top_category = NumberFilter(method='top_category_filter')

    def top_category_filter(self, queryset, name, value):
        return queryset.filter(Q(category_id=value) | Q(category__parent_category_id=value) | Q(
            category__parent_category__parent_category_id=value))
    class Meta:
        model = Goods
        fields = ['is_hot', 'is_new', 'name']
