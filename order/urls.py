from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.order, name='order'),
]