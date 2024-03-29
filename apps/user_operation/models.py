from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from django.db.models import CASCADE
from django.utils import timezone

from goods.models import Goods

User = get_user_model()


class UserFav(models.Model):
    user = models.ForeignKey(User, verbose_name="用户",on_delete=CASCADE)

    goods = models.ForeignKey(Goods, verbose_name="商品",on_delete=CASCADE)
    add_time = models.DateTimeField(default=timezone.now, verbose_name='添加时间')

    class Meta:
        verbose_name = "用户收藏"
        verbose_name_plural = verbose_name

        unique_together = ('user', 'goods')

    def __str__(self):
        return self.user.username



class UserLeavingMessage(models.Model):
    MESSAGE_CHOICES = (
        (1, "留言"),
        (2, "投诉"),
        (3, "询问"),
        (4, "售后"),
        (5, "求购")
    )

    user = models.ForeignKey(User, verbose_name='用户',on_delete=CASCADE)
    message_type = models.CharField(choices=MESSAGE_CHOICES,max_length=10, default=1, verbose_name="留言类型")

    subject = models.CharField(max_length=100, verbose_name="主题", default="")
    message = models.CharField(max_length=1000, verbose_name="留言内容", default="")
    file = models.FileField(upload_to="message/images/", verbose_name="上传的文件", help_text="上传的文件")
    add_time = models.DateTimeField(default=timezone.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "用户留言"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.subject


class UserAddress(models.Model):
    """
    用户收货地址
    """
    user = models.ForeignKey(User, verbose_name="用户", on_delete=CASCADE)
    province = models.CharField(max_length=100, default="", verbose_name="省份")
    city = models.CharField(max_length=100, default="", verbose_name="城市")
    district = models.CharField(max_length=100, default="", verbose_name="区域")
    address = models.CharField(max_length=100, default="", verbose_name="详细地址")
    signer_name = models.CharField(max_length=100, default="", verbose_name="签收人")
    signer_mobile = models.CharField(max_length=11, default="", verbose_name="电话")
    add_time = models.DateTimeField(default=timezone.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "收货地址"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.address


