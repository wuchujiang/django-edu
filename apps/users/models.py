from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.utils import timezone

genderChoice = (
    ('male', '男'),
    ('female', '女'),
)


class UserProfile(AbstractUser):
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name='姓名')

    birthday = models.DateField(null=True, blank=True, verbose_name='出生日期')

    gender = models.CharField(max_length=6, choices=genderChoice, default="female", verbose_name='性别')

    mobile = models.CharField(null=True, blank=True, max_length=11, verbose_name='电话')

    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name='邮箱')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class VerifyCode(models.Model):
    code = models.CharField(max_length=10, verbose_name='验证码')
    mobile = models.CharField(max_length=11, verbose_name='手机号')
    add_time = models.DateTimeField(default=timezone.now, verbose_name='创建时间')

    class Meta:
        verbose_name = '短信验证码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code
