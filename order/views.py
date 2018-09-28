# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import transaction
from django.shortcuts import render
from df_user.user_decorator import decorator
from df_user.models import *
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
    context = {'username': uname, 'users': users}
    return render(request, 'order/place_order.html', context)

