from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login', views.login, name='login'),
    url(r'^forgotpassword/(?P<user_id>[0-9]+)$', views.forgotpassword, name='forgotpassword'),
    url(r'^changepassword/(?P<user_id>[0-9]+)$', views.changepassword, name='changepassword'),


    url(r'^profile/(?P<user_id>[0-9]+)$', views.profile, name='profile'),
    url(r'^profile/(?P<user_id>[0-9]+)/privacy$', views.privacy, name='privacy'),

    url(r'^profile/(?P<user_id>[0-9]+)/personaledit$', views.personaledit, name='personaledit'),
    url(r'^profile/(?P<user_id>[0-9]+)/academicedit$', views.academicedit, name='academicedit'),
    url(r'^profile/(?P<user_id>[0-9]+)/awardedit$', views.awardedit, name='awardedit'),
    url(r'^profile/(?P<user_id>[0-9]+)/workedit$', views.workedit, name='workedit'),

    url(r'^profile/(?P<user_id>[0-9]+)/academic$', views.academic, name='academic'),
    url(r'^profile/(?P<user_id>[0-9]+)/award$', views.award, name='award'),
    url(r'^profile/(?P<user_id>[0-9]+)/work$', views.work, name='work'),

    url(r'^profile/(?P<user_id>[0-9]+)/profilepage$', views.profilepage, name='profilepage'),

    url(r'^organization', views.organization, name='organization'),
    url(r'^aboutus', views.aboutus, name='aboutus'),


]
