# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class OrderInfo(models.Model):
    oid = models.IntegerField(primary_key=True)
    user = models.ForeignKey('df_user.UserInfo')
    odata = models.DateTimeField(auto_now=True)
    oIsPay = models.BooleanField(default=False)
    ototal = models.DecimalField(max_digits=6, decimal_places=2)
    oaddress = models.CharField(max_length=150)

    class Meta:
        db_table = 'orderinfo'


class OrderDetailInfo(models.Model):
    goods = models.ForeignKey('goods.GoodsInfo')
    order = models.ForeignKey('OrderInfo')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    count = models.IntegerField()

    class Meta:
        db_table = 'orderdetail'


