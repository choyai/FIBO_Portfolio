from django.conf.urls import url
from . import views

urlpatterns = [
    # /activities/
    url(r'^$', views.index, name='index'),
    # /activities/create
    url(r'^create$', views.createActivity, name='create'),
    # /activities/activity/
    #url(r'^activity$', views.activity, name='ActivityPage'),
]
