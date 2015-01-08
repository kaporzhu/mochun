# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView

from works.models import Album, Work


class HomeView(TemplateView):
    template_name = 'portals/home.html'

    def get_context_data(self, **kwargs):
        data = super(HomeView, self).get_context_data(**kwargs)
        data.update({
            'albums': Album.objects.all().order_by('-index'),
            'works': Work.objects.filter(visible=True)[:10]
        })
        return data
