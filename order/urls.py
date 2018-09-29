from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.order, name='order'),
    url(r'^create_order/$', views.create, name='create'),
]