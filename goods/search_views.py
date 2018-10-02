# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from haystack.views import SearchView
from df_user.models import *
from goods.models import *
from cart.models import *


class MySearchView(SearchView):
    def extra_context(self):
        content = super(MySearchView, self).extra_context()
        content['title'] = '搜索'
        content['uname'] = uname = self.request.session['uname']  # session 状态保持
        uid = UserInfo.objects.get(username=uname)
        cart = CartInfo.objects.filter(user_id=uid)
        count = cart.count()
        content['cart_count'] = count
        return content
