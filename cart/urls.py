from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.cart, name='cart'),
    url(r'^add(\d+)_(\d+)$', views.add_to_cart, name='add'),
    url(r'^delete(\d+)/$', views.delete, name='delete'),
    url(r'^buy(\d+)_(\d+)', views.buy, name='buy'),
    url(r'^edit(\d+)_(\d+)/', views.edit, name='edit'),
]


