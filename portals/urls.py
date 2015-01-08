# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView

from .views import HomeView


urlpatterns = patterns(
    '',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^me/$', TemplateView.as_view(template_name='portals/me.html'), name='me'),
)
