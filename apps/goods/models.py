from datetime import datetime

from django.db import models

# Create your models here.
from django.db.models import CASCADE

from DUEditor.models import UEditorField

CATEGORY_TYPE = (
    (1, "一级类目"),
    (2, "二级类目"),
    (3, "三级类目"),
)

class GoodCategory(models.Model):

    name = models.CharField(default='', max_length=30, verbose_name="类别名", help_text="类别名")
    code = models.CharField(default='', max_length=30, verbose_name="类别编码")
    desc = models.TextField(default='', verbose_name="描述")

    category_type = models.IntegerField(choices=CATEGORY_TYPE, verbose_name="类目级别",)

    parent_category = models.ForeignKey("self", null=True, blank=True, verbose_name="父类别", on_delete=CASCADE)

    is_tab = models.BooleanField(default=False, verbose_name="是否导航")

    add_time = models.DateTimeField(default=datetime.now(), verbose_name="创建时间")

    class Meta:
        verbose_name = "商品类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name



class Goods(models.Model):
    category = models.ForeignKey(GoodCategory, verbose_name="商品类别",on_delete=CASCADE)
    goods_sn = models.CharField(max_length=50,default='', verbose_name='商品唯一货号')

    name = models.CharField(max_length=100, verbose_name="商品名称")
    click_num = models.IntegerField(default=0, verbose_name="点击数")
    sold_num = models.IntegerField(default=0, verbose_name="销售量")
    fav_num = models.IntegerField(default=0, verbose_name="收藏数量")
    market_price = models.FloatField(default=0, verbose_name="本店价格")
    goods_brief = models.TextField(max_length=500, verbose_name="商品简短描述")
    goods_desc = UEditorField(verbose_name=u"内容", imagePath="goods/images/", width=1000, height=300,
                              filePath="goods/files/", default='')
    ship_free = models.BooleanField(default=True, verbose_name="是否承担运费")
    goods_front_image = models.ImageField(upload_to="goods/images/", null=True, blank=True, verbose_name="封面图")
    is_new = models.BooleanField(default=False, verbose_name="是否新品")
    is_hot = models.BooleanField(default=False, verbose_name="是否热销")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class IndexAd(models.Model):
    category = models.ForeignKey(GoodCategory, related_name="category", verbose_name="商品类目",on_delete=CASCADE)
    goods = models.ForeignKey(Goods,related_name="goods",on_delete=CASCADE)

    class Meta:
        verbose_name = '首页商品类别广告'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


class GoodsImage(models.Model):
    """
    商品轮播图
    """
    goods = models.ForeignKey(Goods, verbose_name="商品", related_name="images", on_delete=CASCADE)
    image = models.ImageField(upload_to="", verbose_name="图片", null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '商品图片'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


class Banner(models.Model):
    """
    轮播的商品
    """
    goods = models.ForeignKey(Goods, verbose_name="商品", on_delete=CASCADE)
    image = models.ImageField(upload_to='banner', verbose_name="轮播图片")
    index = models.IntegerField(default=0, verbose_name="轮播顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '轮播商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


class HotSearchWords(models.Model):
    """
    热搜词
    """
    keywords = models.CharField(default="", max_length=20, verbose_name="热搜词")
    index = models.IntegerField(default=0, verbose_name="排序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '热搜词'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.keywords