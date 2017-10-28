from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^create', views.create, name='create'),
    url(r'^ActivityPage', views.activity, name='activity'),
]
