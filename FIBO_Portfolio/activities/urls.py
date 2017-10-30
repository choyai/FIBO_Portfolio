from django.conf.urls import url
from . import views
from django.contrib.auth.models import User

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^create', views.create, name='create'),
    url(r'^edit', views.edit, name='edit'),
    url(r'^activity/(?P<activity_id>[0-9]+)$', views.activity, name='activity'),
    url(r'^(?P<user_id>[0-9]+)/activities', views.myactivities, name='myactivities'),
]
