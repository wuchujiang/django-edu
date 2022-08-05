
from rest_framework import serializers

from goods.models import Goods, GoodCategory


class GoodCategorySerializer(serializers.ModelSerializer):
    category_type_name = serializers.SerializerMethodField(read_only=True)

    def get_category_type_name(self, obj):
        return obj.get_category_type_display()

    class Meta:
        model = GoodCategory
        fields = "__all__"

class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = "__all__"


class GoodDetailSerializer(serializers.ModelSerializer):
    category = GoodCategorySerializer()

    class Meta:
        model = Goods
        fields = "__all__"

