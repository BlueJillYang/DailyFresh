# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class UserInfo(models.Model):
    username = models.CharField(max_length=20, null=False, blank=False)
    password = models.CharField(max_length=40)
    email = models.CharField(max_length=20, null=False, blank=False)
    uaddress = models.CharField(max_length=40, default='')
    zipcode = models.IntegerField(default=0)
    phonecall = models.IntegerField(default=0)
    receiver = models.CharField(max_length=10, default='')

    class Meta:
        db_table = 'userinfo'


class Address(models.Model):
    address = models.CharField(max_length=40)
    user = models.ForeignKey('UserInfo')

    class Meta:
        db_table = 'address'


