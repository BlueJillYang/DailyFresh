# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from tinymce.models import HTMLField
from django.db import models

# Create your models here.


class TypeInfo(models.Model):
    t_title = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.t_title.encode('utf-8')

    class Meta:
        db_table = 'typeinfo'


class GoodsInfo(models.Model):
    g_title = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    picture = models.ImageField(upload_to='goods')  # 想要上传图片 需要在settings中设置MEDIA_ROOT属性
    unit = models.CharField(max_length=20)  # 单位 500g 1kg 1个 1升
    click = models.IntegerField()  # 点击量 代表人气
    summary = models.CharField(max_length=200)  # 商品简介
    content = HTMLField()
    reserve = models.IntegerField()  # 库存

    isDelete = models.BooleanField(default=False)
    type = models.ForeignKey('TypeInfo')

    class Meta:
        db_table = 'goodsinfo'
