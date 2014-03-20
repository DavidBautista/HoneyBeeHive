from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    #COMMON
    url(r'^features/$', 'project_management.views.common.features', name='features'),
    url(r'^pricing/$', 'project_management.views.common.pricing', name='pricing'),
    url(r'^help_and_community/$', 'project_management.views.common.help_and_community', name='help_and_community'),
    url(r'^about/$', 'project_management.views.common.about', name='about'),

    #AUTH
    url(r'^login/$', 'project_management.views.auth.login_user', name='login'),
    url(r'^register/$', 'project_management.views.auth.register',  name='register'),
    url(r'^activate_email/$', 'project_management.views.auth.activate', name='activate_email'),

    #PROJECTS, SPRINTS & TASKS
    url(r'^projects/$', 'project_management.views.psttasks.projects', name='projects_list'),
    url(r'^project/(?P<proj_id>\d+)/$', 'project_management.views.psttasks.project', name='project'),
    url(r'^create_project/$', 'project_management.views.psttasks.create_project', name='create_project'),

    #PROFILE SUMMARY

    #MESSAGING & DISCUSSION

)