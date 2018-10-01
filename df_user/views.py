# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.paginator import Paginator

from cart.models import CartInfo
from .user_decorator import decorator
from django.http import JsonResponse
from django.shortcuts import render, redirect
import hashlib
from .models import *
from goods.models import *
from order.models import *

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


def login(request):
    context = {'title': '登录'}
    return render(request, 'df_user/login.html', context)


def register(request):
    context = {'title': '注册'}
    return render(request, 'df_user/register.html', context)


def register_exist(request):
    uname = request.GET.get('uname')
    count = UserInfo.objects.filter(username=uname).count()
    return JsonResponse({'count': count})


def register_handle(request):
    user_name = request.POST['user_name']
    pwd = request.POST['pwd']
    cpwd = request.POST['cpwd']
    email = request.POST['email']
    userinfo = UserInfo()
    if UserInfo.objects.filter(username=user_name):
        return redirect('/register/')
    else:
        if pwd != cpwd:
            return redirect('/register/')
        elif pwd == cpwd:
            sha = hashlib.sha1()
            sha.update(cpwd.encode('utf-8'))
            passwd = sha.hexdigest()
            userinfo.username = user_name
            userinfo.password = passwd
            userinfo.email = email
            userinfo.save()
            return redirect('/login/')


def login_handle(request):
    post = request.POST
    uname = post.get('username', '')
    upwd = post.get('pwd', '')
    # 定义用户名，密码错误时的属性
    name_error = 0
    pwd_error = 0

    # 密码加密
    if uname:
        sha = hashlib.sha1()
        sha.update(upwd.encode('utf-8'))
        pwd = sha.hexdigest()
        list = UserInfo.objects.filter(username=uname)

        # 验证用户名是否存在
        if list:
            if list[0].password == pwd and upwd is not None:
                request.session['uname'] = uname
                request.session.set_expiry(0)
                full_path = request.COOKIES.get('url', '')
                if len(full_path) > 1:
                    return redirect(full_path)
                else:
                    return redirect('/user_center/')  # 用户名及密码验证正确后 即可进入用户中心/首页
            elif list[0].password != pwd:
                pwd_error = 1
        else:  # 用户名不存在时，ajax显示用户名不存在，并把之前的用户名显示在文本框内
            name_error = 1
    context = {'uname': uname, 'upwd': upwd, 'name_error': name_error, 'pwd_error': pwd_error}
    return render(request, 'df_user/login.html', context)


@decorator
def user_center(request):
    uname = request.session.get('uname', '')
    user = UserInfo.objects.filter(username=uname)[0]
    phone_number = user.phonecall
    address = user.uaddress

    # 最近浏览
    try:
        list = request.COOKIES.get('goods_ids', '').split(',')
        view_ago = []
        for ids in list:
            view_ago.append(GoodsInfo.objects.get(id=int(ids)))
    except Exception:
        pass

    context = {'title': '用户中心', 'username': uname, 'phonenumber': phone_number, 'address': address, 'view_ago': view_ago}
    return render(request, 'df_user/user_center_info.html', context)


@decorator
def user_center_order(request):
    uname = request.session.get('uname', '')
    user1 = UserInfo.objects.get(username=uname)
    uid = user1.id
    order = OrderInfo.objects.filter(user_id=uid).order_by('-oid')  # 查询用户的订单 复数
    # 页数 paginator
    paginator = Paginator(order, 2)
    page = paginator.page(1)
    context = {'title': '用户中心', 'username': uname, 'page': page}
    return render(request, 'df_user/user_center_order.html', context)


def user_center_order_handle(request, pagenumber):
    uname = request.session.get('uname', '')
    uid = UserInfo.objects.get(username=uname).id
    order = OrderInfo.objects.filter(user_id=uid).order_by('-oid')  # 查询用户的订单 复数
    # 页数 paginator
    paginator = Paginator(order, 2)
    pagenumber = int(pagenumber)
    if not pagenumber:
        page = paginator.page(1)
    else:
        page = paginator.page(pagenumber)

    context = {'title': '用户中心', 'username': uname, 'order': order, 'page': page}
    return render(request, 'df_user/user_center_order.html', context)


@decorator
def user_center_site(request):
    uname = request.session.get('uname', '')
    detail_address = UserInfo.objects.get(username=uname).uaddress
    context = {'title': '用户中心', 'username': uname, 'detail_address': detail_address}
    return render(request, 'df_user/user_center_site.html', context)


@decorator
def user_center_site_handle(request):
    # 存储属性信息
    post = request.POST
    receiver = post.get('receiver')
    site_area = post.get('site_area')
    zip_code = post.get('zip_code')
    phone_number = post.get('phone_number')

    # 要拿到当前登录的用户名，然后对此用户的信息进行添加
    uname = request.session.get('uname', '')
    user = UserInfo.objects.filter(username=uname)[0]
    user.receiver = receiver
    user.phonecall = int(phone_number)
    user.zipcode = int(zip_code)
    user.uaddress = site_area
    user.save()

    # 外键链接
    addr = Address()
    addr.address = site_area
    addr.user_id = user.id
    addr.save()
    return redirect('/user_center_site/')

def exit_handle(request):
    uname = request.session.get('uname', '')
    if len(uname) > 1:
        del request.session['uname']
    return redirect('/index/')

