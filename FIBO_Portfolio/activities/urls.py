from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^create', views.create, name='create'),
    url(r'^edit', views.edit, name='edit'),
    url(r'^ActivityPage', views.activity, name='activity'),
    url(r'^myactivity/(?P<user_id>[0-9])', views.myactivity, name='myactivity'),

]
