# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from df_user.user_decorator import decorator
from django.core.paginator import Paginator
from .models import *
from django.shortcuts import render
from df_user.models import *
from cart.models import *

# Create your views here.


def index(request):
    uname = request.session.get('uname', '')
    # 首页 6大类
    goods1 = GoodsInfo.objects.filter(type_id=1)
    goods11 = GoodsInfo.objects.filter(type_id=1).order_by('-id')

    goods2 = GoodsInfo.objects.filter(type_id=2)
    goods21 = GoodsInfo.objects.filter(type_id=2).order_by('-id')

    goods3 = GoodsInfo.objects.filter(type_id=3)
    goods31 = GoodsInfo.objects.filter(type_id=3).order_by('-id')

    goods4 = GoodsInfo.objects.filter(type_id=4)
    goods41 = GoodsInfo.objects.filter(type_id=4).order_by('-id')

    goods5 = GoodsInfo.objects.filter(type_id=5)
    goods51 = GoodsInfo.objects.filter(type_id=5).order_by('-id')

    goods6 = GoodsInfo.objects.filter(type_id=6)
    goods61 = GoodsInfo.objects.filter(type_id=6).order_by('-id')

    uid = UserInfo.objects.get(username=uname).id
    ucart = CartInfo.objects.filter(user_id_id=uid)  # 此用户对应的cart对象
    count = ucart.count()
    context = {'title': '首页', 'uname': uname,
               'goods1': goods1, 'goods2': goods2,
               'goods11': goods11, 'goods21': goods21,
               'goods3': goods3, 'goods4': goods4,
               'goods31': goods31, 'goods41': goods41,
               'goods51': goods51, 'goods61': goods61,
               'goods5': goods5, 'goods6': goods6, 'cart_count': count}
    return render(request, 'goods/index.html', context)


def detail(request, id):
    uname = request.session.get('uname', '')
    goods = GoodsInfo.objects.get(id=id)
    type = TypeInfo.objects.get(id=goods.type_id)
    goods.click += 1
    goods.save()

    uid = UserInfo.objects.get(username=uname).id
    ucart = CartInfo.objects.filter(user_id_id=uid)  # 此用户对应的cart对象
    count = ucart.count()

    list = GoodsInfo.objects.filter(type_id=goods.type_id).order_by('-id')[:2]
    context = {'title': '商品详情', 'uname': uname, 'goods': goods, 'list': list, 'type': type, 'cart_count': count}
    response = render(request, 'goods/detail.html', context)

    # 最近浏览功能 点了详情页面 视为最近浏览
    goods_ids = request.COOKIES.get('goods_ids', '')
    goods_id = '%d'%goods.id
    if goods_ids != '':
        goods_ids1 = goods_ids.split(',')  # 拆分为列表
        if goods_ids1.count(goods_id) >= 1:  # 如果出现了一次 就删掉
            goods_ids1.remove(goods_id)
        goods_ids1.insert(0, goods_id)  # 删除后 把现有的id加到第一个
        if len(goods_ids1) >= 6:  # 如果超过5个 就删 保证只有5个最近浏览
            del goods_ids1[5:]
        goods_ids = ','.join(goods_ids1)  # 拼接为字符串
    else:
        goods_ids = goods_id
    response.set_cookie('goods_ids', goods_ids)
    return response


def list(request, type, sort, pagenumber):  # type类别 id编号 sort排序规则 pagenumber页数
    uname = request.session.get('uname', '')

    Type = TypeInfo.objects.get(id=type)
    list = Type.goodsinfo_set.all()
    latest = list.order_by('-id')[:2]
    if int(sort) == 1:
        list = Type.goodsinfo_set.all().order_by('-price')
    if int(sort) == 2:
        list = Type.goodsinfo_set.all().order_by('-click')

    paginator = Paginator(list, 5)
    if not pagenumber:
        page = paginator.page(1)
    else:
        page = paginator.page(pagenumber)

    uid = UserInfo.objects.get(username=uname).id
    ucart = CartInfo.objects.filter(user_id_id=uid)  # 此用户对应的cart对象
    count = ucart.count()

    context = {'title': '商品列表', 'uname': uname, 'list': list,
               'latest': latest, 'page': page, 'type': Type,
               'cart_count': count, 'sort': int(sort)}
    return render(request, 'goods/list.html', context)



