from django.conf.urls import url
import views

urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^detail/(\d+)', views.detail, name='detail'),
    url(r'^list_(\d)_(\d)/(\d?)', views.list, name='list'),
]