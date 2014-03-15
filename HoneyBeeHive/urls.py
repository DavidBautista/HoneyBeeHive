from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns

urlpatterns = i18n_patterns('',
    url(r'^', include('project_management.urls')),
    url(r'^$', 'project_management.views.common.index', name='index'),
)
