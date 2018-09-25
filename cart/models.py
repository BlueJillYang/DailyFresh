# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class CartInfo(models.Model):
    user_id = models.ForeignKey('df_user.UserInfo')
    goods_id = models.ForeignKey('goods.GoodsInfo')
    amount = models.IntegerField()

    class Meta:
        db_table = 'cartinfo'


