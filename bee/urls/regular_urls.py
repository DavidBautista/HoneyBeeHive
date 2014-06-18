from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    #COMMON

    #AUTH
    url(r'^logout/$', 'bee.views.auth.logout_user', name='logout'),
    #PROJECTS, SPRINTS & TASKS

    #PROFILE SUMMARY

    #MESSAGING & DISCUSSION

    #API
    url(r'^api/', include('bee.api.urls'))

)
