# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import transaction
from django.shortcuts import render
from df_user.user_decorator import decorator
from df_user.models import *
from .models import *
from goods.models import *
from cart.models import *

# Create your views here.


# 如何使用事务 point=transaction.savepoint() 保存一个点
# 回退 transaction.savepoint_rollback(point)
# 提交 transaction.savepoint_commit(point)
@transaction.atomic()
@decorator
def order(request):
    uname = request.session.get('uname', '')
    users = UserInfo.objects.get(username=uname)
    # 接收参数
    cart_ids = request.GET.getlist('cart_id')

    cart = []
    for cart_id in cart_ids:
        cart.append(CartInfo.objects.filter(user_id_id=users.id, goods_id_id=cart_id)[0])

    context = {'username': uname, 'users': users, 'cart': cart}
    return render(request, 'order/place_order.html', context)


@transaction.atomic()
@decorator
def create(request):
    uname = request.session.get('uname', '')
    users = UserInfo.objects.get(username=uname)
    # 接收参数
    cart_ids = request.GET.getlist('cart_id')
    cart = []
    for cart_id in cart_ids:
        cart.append(CartInfo.objects.filter(user_id_id=users.id, goods_id_id=cart_id)[0])
    # 创建事务保存点
    transPoint = transaction.savepoint()

    # 创建order对象
    order = OrderInfo()
    try:
        order.oid = 1
        order.user_id = users.id
        order.oIsPay = True
    except Exception as e:
        # 异常就回滚数据 报错
        transaction.savepoint_rollback(transPoint)
    else:
        # 成功就提交
        transaction.savepoint_commit(transPoint)

    return render(request, 'order/pay.html')
