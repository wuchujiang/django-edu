from rest_framework import serializers

from goods.models import Goods, GoodCategory, GoodsImage, HotSearchWords, Banner, GoodsCategoryBrand


class GoodCategorySerializer3(serializers.ModelSerializer):
    class Meta:
        model = GoodCategory
        fields = "__all__"


class GoodCategorySerializer2(serializers.ModelSerializer):
    sub_cat = GoodCategorySerializer3(many=True)

    class Meta:
        model = GoodCategory
        fields = "__all__"


class GoodCategorySerializer(serializers.ModelSerializer):
    # sub_cat = GoodCategorySerializer2(many=True)

    class Meta:
        model = GoodCategory
        fields = "__all__"


class GoodImageSerializer(serializers.ModelSerializer):
    # goods = GoodsSerializer()

    class Meta:
        model = GoodsImage
        fields = "__all__"


class GoodsSerializer(serializers.ModelSerializer):
    category = GoodCategorySerializer()

    # def get_images(self, obj):
    #     return GoodImageSerializer(GoodsImage.objects.filter(goods_id=obj.id), many=True).data

    # images = GoodImageSerializer(many=True)
    #
    # def get_images(self,obj):
    #     return []

    class Meta:
        model = Goods
        fields = "__all__"


class GoodsDetailSerializer(serializers.ModelSerializer):
    category = GoodCategorySerializer()

    class Meta:
        model = Goods
        fields = "__all__"


class HotWordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotSearchWords
        fields = "__all__"


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategoryBrand
        fields = "__all__"
