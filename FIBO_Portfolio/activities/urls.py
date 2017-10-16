from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.activities_home, name='activities_home'),
    url(r'^create', views.create, name='create'),
]
