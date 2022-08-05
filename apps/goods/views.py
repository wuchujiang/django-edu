from django.shortcuts import render

# Create your views here.
from rest_framework.generics import GenericAPIView, ListAPIView, DestroyAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from goods.models import Goods

from goods.serializers import GoodsSerializer, GoodDetailSerializer


class GoodsView(ModelViewSet):
    serializer_class = GoodsSerializer
    queryset = Goods.objects.all()
    filter_fields = ['id']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return GoodDetailSerializer

        return GoodsSerializer
    # def get(self, request):
    #     goods = self.get_queryset()
    #     print(goods)
    #     data = self.get_serializer(goods, many=True)
    #     return Response(data.data)

    # def get(self, request):
    #     return self.list(request)

    # def post(self, request):
    #     data = request.data
    #     ser = self.get_serializer(data=data)
    #     ser.is_valid(raise_exception=True)
    #     ser.save()
    #     return Response(ser.data)
