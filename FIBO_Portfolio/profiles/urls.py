from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

app_name = 'profiles'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/$', auth_views.login, {'template_name':'profiles/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^register$', views.UserFormView.as_view(), name='register'),
    url(r'^changepassword/(?P<pk>[0-9]+)$', views.changepassword, name='changepassword'),

    url(r'^password_reset/$', auth_views.password_reset,{'template_name':'profiles/reset_password.html',
                                                    'post_reset_redirect':'profiles:password_reset_done',
                                                    'from_email':'fibo.portfolio@gmail.com'
                                                    },
                                                    name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done,{'template_name':'profiles/password_reset_done.html'}, name='password_reset_done'),
    url(r'^password_reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)$', auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^password_reset/complete/$', auth_views.password_reset_complete, name='password_reset_complete'),



    url(r'^profile/(?P<pk>[0-9]+)$', views.ProfileView.as_view(), name='profile'),
    url(r'^profile/(?P<user_id>[0-9]+)/privacy$', views.privacy, name='privacy'),
    url(r'^profile/(?P<pk>[0-9]+)/edit$', views.ProfileUpdate.as_view(), name='personaledit'),


    url(r'^profile/(?P<pk>[0-9]+)/academic$', views.AcademicView.as_view(), name='academic'),
    url(r'^profile/(?P<pk>[0-9]+)/award$', views.AwardView.as_view(), name='award'),
    url(r'^profile/(?P<pk>[0-9]+)/work$', views.WorkView.as_view(), name='work'),

    url(r'^organization', views.organization, name='organization'),
    url(r'^organization/executive_team$', views.ExecutiveTeamView.as_view(), name='executive_team'),
    url(r'^organization/lecturers_and_researchers$', views.LecturerAndResearcherView.as_view(), name='lecturers_and_researchers'),
    url(r'^organization/adjunct_lecturers$', views.AdjunctionLecturerView.as_view(), name='adjunct_lecturers'),
    url(r'^organization/engineers$', views.EngineersView.as_view(), name='engineers'),
    url(r'^organization/officers$', views.OfficerView.as_view(), name='officers'),
    url(r'^organization/students$', views.StudentView.as_view(), name='students'),


    url(r'^aboutus', views.aboutus, name='aboutus'),


]
