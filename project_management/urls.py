from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    #AUTH
    url(r'^login/$', 'project_management.views.auth.login_user'),
    url(r'^logout/$', 'project_management.views.auth.logout_user'),
    url(r'^register/$', 'project_management.views.auth.register'),
    url(r'^activate_email/$', 'project_management.views.auth.activate'),


)
