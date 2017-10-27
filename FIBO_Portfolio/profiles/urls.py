from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^profile/(?P<user_id>[0-9]+)$', views.profile, name='profile'),
    url(r'^profile/(?P<user_id>[0-9]+)/edit$', views.edit, name='edit'),
    url(r'^profile/(?P<user_id>[0-9]+)/academic$', views.edit, name='academic'),
    url(r'^profile/(?P<user_id>[0-9]+)/award$', views.edit, name='award'),
    url(r'^profile/(?P<user_id>[0-9]+)/changepassword$', views.edit, name='changepassword'),
    url(r'^profile/(?P<user_id>[0-9]+)/privacy$', views.edit, name='privacy'),
    url(r'^profile/(?P<user_id>[0-9]+)/profilepage$', views.edit, name='profilepage'),
    url(r'^profile/(?P<user_id>[0-9]+)/work$', views.edit, name='work'),
    url(r'^organization', views.organization, name='organization')
]
