from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.activities_home, name='home'),
    url(r'^create', views.create, name='create'),
]
