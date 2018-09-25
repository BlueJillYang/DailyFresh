# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.contrib import admin

# Register your models here.


class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 't_title']


@admin.register(GoodsInfo)
class GoodsInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'g_title', 'type_id']


admin.site.register(TypeInfo, TypeInfoAdmin)
