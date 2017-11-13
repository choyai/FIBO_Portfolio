from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import (password_reset, password_reset_done, password_reset_confirm
, password_reset_commplete)

app_name = 'profiles'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/$', auth_views.login, {'template_name':'profiles/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^register$', views.UserFormView.as_view(), name='register'),
    url(r'^changepassword/(?P<pk>[0-9]+)$', views.changepassword, name='changepassword'),

    url(r'^reset-password/$'), change_password, name='change_password'),
    url(r'^reset-password/done/$'), change_password_done, name='change_password_done'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)$'), change_password_confirm, name='change_password_confirm'),
    url(r'^reset-password/complete/$'), change_password_complete, name='change_password_complete'),



    url(r'^profile/(?P<pk>[0-9]+)$', views.ProfileView.as_view(), name='profile'),
    url(r'^profile/(?P<user_id>[0-9]+)/privacy$', views.privacy, name='privacy'),

    url(r'^profile/(?P<pk>[0-9]+)/edit$', views.ProfileUpdate.as_view(), name='personaledit'),


    url(r'^profile/(?P<pk>[0-9]+)/academic$', views.AcademicView.as_view(), name='academic'),
    url(r'^profile/(?P<pk>[0-9]+)/award$', views.AwardView.as_view(), name='award'),
    url(r'^profile/(?P<pk>[0-9]+)/work$', views.WorkView.as_view(), name='work'),

    url(r'^organization', views.organization, name='organization'),
    url(r'^aboutus', views.aboutus, name='aboutus'),


]
