# Generated by Django 3.2.9 on 2022-08-05 11:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_alter_goodcategory_add_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodcategory',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 5, 11, 39, 35, 382894), verbose_name='创建时间'),
        ),
    ]
