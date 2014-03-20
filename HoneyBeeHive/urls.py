from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.views.generic import RedirectView
from HoneyBeeHive import settings

#url with language code prepend
urlpatterns = i18n_patterns('',
    url(r'^$', 'project_management.views.common.index', name='index'),
    url(r'^', include('project_management.urls.trans_urls')),
)

#regular urls
urlpatterns += patterns('',
    url(r'^', include('project_management.urls.regular_urls')),
    (r'^favicon\.ico$', RedirectView.as_view(url=settings.STATIC_URL + 'img/favicon.ico')),
)

