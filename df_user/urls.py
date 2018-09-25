from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^login/$', views.login, name='login'),
    url(r'^login_handle/$', views.login_handle, name='login_handle'),
    url(r'^register/$', views.register, name='register'),
    url(r'^register_handle/$', views.register_handle, name='register_handle'),
    url(r'^register_exist/', views.register_exist, name='register_exist'),
    url(r'^user_center/$', views.user_center, name='user_center'),
    url(r'^user_center_info/$', views.user_center, name='user_center'),
    url(r'^user_center_site/$', views.user_center_site, name='user_center_site'),
    url(r'^user_center_site_handle/$', views.user_center_site_handle, name='user_center_site_handle'),
    url(r'^user_center_order/$', views.user_center_order, name='user_center_order'),
    url(r'^exit/', views.exit_handle, name='exit_handle'),
]

