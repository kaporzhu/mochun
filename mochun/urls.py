from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns(
    '',
    url(r'^', include('portals.urls', 'portals', 'portals')),
    url(r'^works/', include('works.urls', 'works', 'works')),
    url(r'^admin/', include(admin.site.urls)),
)
