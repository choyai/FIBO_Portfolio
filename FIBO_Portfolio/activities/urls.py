from django.conf.urls import url
from . import views
from django.contrib import  admin
from django.contrib.auth.models import User

app_name = 'activities'

urlpatterns = [
    url(r'^$', views.ActivitiesIndex.as_views(), name='home'),
    url(r'^(?P<pk>[0-9]+)/$', view.ActivitiesDetail.as_views(), name='detail'),
    url(r'^activities/createActivities/$', views.ActivitiesCreate.as_view(), name='create')

    url(r'^edit', views.edit, name='edit'),
    url(r'^ActivityPage', views.activity, name='activity'),
    url(r'^(?P<user_id>[0-9]+)/activities', views.myactivities, name='myactivities'),
]