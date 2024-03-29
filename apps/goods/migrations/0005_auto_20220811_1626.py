# Generated by Django 3.2.9 on 2022-08-11 16:26

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_auto_20220809_1808'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='goods_num',
            field=models.IntegerField(default=0, verbose_name='库存数'),
        ),
        migrations.AddField(
            model_name='goods',
            name='shop_price',
            field=models.FloatField(default=0, verbose_name='本店价格'),
        ),
        migrations.AlterField(
            model_name='goodcategory',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 11, 16, 26, 23, 810241), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='goodcategory',
            name='parent_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_cat', to='goods.goodcategory', verbose_name='父类别'),
        ),
    ]
