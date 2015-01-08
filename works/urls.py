# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from .views import(
    WorkListView, CreateWorkView, CreateAlbumView, ChangeAlbumOrderView,
    ChangeWorkOrderView, UpdateWorkView, UpdateAlbumView, DeleteWorkView,
    DeleteAlbumView, ToggleWorkView, AlbumWorksView
)


urlpatterns = patterns(
    '',
    url(r'^$', WorkListView.as_view(), name='list'),
    url(r'^create/$', CreateWorkView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/update/$', UpdateWorkView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', DeleteWorkView.as_view(), name='delete'),
    url(r'^(?P<pk>\d+)/toggle/$', ToggleWorkView.as_view(), name='toggle'),
    url(r'^create_album/$', CreateAlbumView.as_view(), name='create_album'),
    url(r'^album_works/$', AlbumWorksView.as_view(), name='album_works'),
    url(r'^(?P<pk>\d+)/update_album/$', UpdateAlbumView.as_view(), name='update_album'),
    url(r'^(?P<pk>\d+)/delete_album/$', DeleteAlbumView.as_view(), name='delete_album'),
    url(r'^change_album_order/$', ChangeAlbumOrderView.as_view(), name='change_album_order'),
    url(r'^change_work_order/$', ChangeWorkOrderView.as_view(), name='change_work_order'),
)