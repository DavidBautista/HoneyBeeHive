from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^', include('project_management.urls')),
    url(r'^$', 'project_management.views.common.index'),
)
