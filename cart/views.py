# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse

from df_user.user_decorator import *
from django.shortcuts import render, redirect
from df_user.models import *
from goods.models import *
from .models import CartInfo

# Create your views here.


@decorator
def cart(request):
    uname = request.session['uname']
    uid = UserInfo.objects.get(username=uname).id
    ucart = CartInfo.objects.filter(user_id_id=uid)  # 此用户对应的cart对象
    count = ucart.count()
    context = {'ucart': ucart, 'username': uname, 'uid': uid, 'cart_count': count}
    return render(request, 'cart/cart.html', context)


@decorator
def add_to_cart(request, gid, amount):
    uname = request.session['uname']
    uid = UserInfo.objects.get(username=uname).id
    carts = CartInfo.objects.filter(user_id_id=uid, goods_id_id=int(gid))
    if len(carts) >= 1:
        cart = carts[0]
        cart.amount += int(amount)
    else:
        cart = CartInfo()
        cart.user_id_id = uid
        cart.goods_id_id = int(gid)
        cart.amount = amount
    cart.save()
    if request.is_ajax():
        count = CartInfo.objects.filter(user_id_id=uid).count()
        data = {'count1': count}
        return JsonResponse(data)
    else:
        return redirect('/cart/')


@decorator
def delete(request, id):
    uname = request.session['uname']
    uid = UserInfo.objects.get(username=uname).id
    cart = CartInfo.objects.filter(user_id_id=uid, goods_id_id=int(id))[0]
    cart.delete()
    return redirect('/cart/')


@decorator
def buy(request, gid):
    uname = request.session['uname']
    uid = UserInfo.objects.get(username=uname).id
    cart = CartInfo.objects.filter(user_id_id=uid, goods_id_id=gid)
    if len(cart) != 0:
        cart[0].amount += 1
    else:
        cart = CartInfo()
        cart.user_id_id = uid
        cart.goods_id_id = gid
        cart.amount = 1
        cart.save()
    return redirect('/cart/')


@decorator
def edit(request, cart_id, amount):
    try:
        cart = CartInfo.objects.get(goods_id_id=int(cart_id))
        cart.amount = int(amount)
        cart.save()
        count = cart.amount
        data = {'ok': 0}
    except Exception as e:
        data = {'ok': count}
    return JsonResponse(data)



