from django.conf.urls import url
from . import views
from django.contrib import  admin
from django.contrib.auth.models import User

app_name = 'activities'

urlpatterns = [
    url(r'^$', views.ActivitiesIndex.as_view(), name='home'),
    url(r'^(?P<pk>[0-9]+)/$', views.ActivitiesDetail.as_view(), name='detail'),
    url(r'^create', views.ActivitiesCreate.as_view(), name='create'),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.ActivitiesUpdate.as_view(), name='update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.ActivitiesDelete.as_view(), name='delete'),
    url(r'^activity/(?P<activity_id>[0-9]+)$', views.activity, name='activity'),
    url(r'^(?P<user_id>[0-9]+)/activities', views.myactivities, name='myactivities'),
]