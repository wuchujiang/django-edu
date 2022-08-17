from django.db.models import Count, Max, Min, Avg, F
from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import GenericAPIView, ListAPIView, DestroyAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from goods.filters import GoodsFilter
from goods.models import Goods, GoodsImage, GoodCategory

from goods.serializers import GoodsSerializer, GoodImageSerializer

from rest_framework_extensions.cache.mixins import CacheResponseMixin


class GoodsPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 100


class GoodsListViewSet(CacheResponseMixin, ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Goods.objects.select_related('category')

    serializer_class = GoodsSerializer
    pagination_class = None

    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_class = GoodsFilter
    search_fields = ('name', 'goods_brief', 'goods_desc')
    ordering_fields = ('shop_price',)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.click_num += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class Svg(object):
    pass


class GoodsListView(ListAPIView):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = None

    def list(self, request, *args, **kwargs):
        category = GoodCategory.objects.annotate(c=Count('goods__id'), test=F("name")).order_by('-c').values(
            'test', 'c')

        # 包含最多商品的分类
        s = Goods.objects.aggregate(c=Count('id'), p=Max('shop_price'), s=Avg('shop_price'), m=Min('shop_price'))
        print(category)
        print(s)


        return Response(category)
        # return super().list(request, *args, **kwargs)