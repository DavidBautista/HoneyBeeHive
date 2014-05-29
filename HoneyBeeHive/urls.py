from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.views.generic import RedirectView
from HoneyBeeHive import settings
from django.contrib import admin

admin.autodiscover()

#url with language code prepend
urlpatterns = i18n_patterns('',
    url(r'^$', 'bee.views.common.index', name='index'),
    url(r'^', include('bee.urls.trans_urls')),
)

#regular urls
urlpatterns += patterns('',
    url(r'^', include('bee.urls.regular_urls')),
    (r'^favicon\.ico$', RedirectView.as_view(url=settings.STATIC_URL + 'img/favicon.ico')),
    url(r'^admin/', include(admin.site.urls)),

)

