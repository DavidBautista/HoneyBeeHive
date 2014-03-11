from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    #COMMON
    url(r'^features/$', 'project_management.views.common.features'),
    url(r'^pricing/$', 'project_management.views.common.pricing'),
    url(r'^help_and_community/$', 'project_management.views.common.help_and_community'),
    url(r'^about/$', 'project_management.views.common.about'),

    #AUTH
    url(r'^login/$', 'project_management.views.auth.login_user'),
    url(r'^logout/$', 'project_management.views.auth.logout_user'),
    url(r'^register/$', 'project_management.views.auth.register'),
    url(r'^activate_email/$', 'project_management.views.auth.activate'),

    #PROJECTS, SPRINTS & TASKS
    url(r'^projects/$', 'project_management.views.psttasks.projects'),
    url(r'^project/(?P<proj_id>\d+)/$', 'project_management.views.psttasks.project', name='project'),
    url(r'^create_project/$', 'project_management.views.psttasks.create_project'),


    #PROFILE SUMMARY


    #MESSAGING & DISCUSSION







)
