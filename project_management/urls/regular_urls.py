from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    #COMMON

    #AUTH
    url(r'^logout/$', 'project_management.views.auth.logout_user', name='logout'),
    #PROJECTS, SPRINTS & TASKS

    #PROFILE SUMMARY

    #MESSAGING & DISCUSSION
)
