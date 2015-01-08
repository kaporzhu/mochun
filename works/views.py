# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse_lazy
from django.db.models import Max
from django.http.response import HttpResponseRedirect
from django.views.generic.base import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from braces.views import(
    SuperuserRequiredMixin, AjaxResponseMixin, JSONResponseMixin
)

from .forms import WorkForm, AlbumForm
from .models import Work, Album


class WorkListView(SuperuserRequiredMixin, ListView):
    model = Album

    def get_queryset(self):
        qs = super(WorkListView, self).get_queryset()
        return qs.order_by('-index')


class CreateWorkView(SuperuserRequiredMixin, CreateView):
    model = Work
    form_class = WorkForm
    success_url = reverse_lazy('works:list')

    def form_valid(self, form):
        work = form.save(commit=False)
        work.album = Album.objects.get(pk=self.request.GET['album_id'])
        index_max = Work.objects.all().aggregate(Max('index'))['index__max']
        if index_max is None:
            index_max = 0
        work.index = index_max + 1
        work.save()
        self.object = work
        return HttpResponseRedirect(self.get_success_url())


class UpdateWorkView(SuperuserRequiredMixin, UpdateView):
    model = Work
    form_class = WorkForm
    success_url = reverse_lazy('works:list')


class DeleteWorkView(SuperuserRequiredMixin, DeleteView):
    model = Work
    success_url = reverse_lazy('works:list')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class ToggleWorkView(SuperuserRequiredMixin, AjaxResponseMixin,
                     JSONResponseMixin, View):

    def get_ajax(self, request, *args, **kwargs):
        work = Work.objects.get(pk=self.kwargs['pk'])
        work.visible = not work.visible
        work.save()
        return self.render_json_response({'visible': work.visible})


class CreateAlbumView(SuperuserRequiredMixin, CreateView):
    model = Album
    form_class = AlbumForm
    success_url = reverse_lazy('works:list')

    def form_valid(self, form):
        album = form.save(commit=False)
        index_max = Album.objects.all().aggregate(Max('index'))['index__max']
        if index_max is None:
            index_max = 0
        album.index = index_max + 1
        album.save()
        self.object = album
        return HttpResponseRedirect(self.get_success_url())


class AlbumWorksView(ListView):
    model = Work
    template_name = 'works/album_works.html'

    def get_queryset(self):
        album = Album.objects.get(pk=self.request.GET['id'])
        return album.visible_works


class UpdateAlbumView(SuperuserRequiredMixin, UpdateView):
    model = Album
    form_class = AlbumForm
    success_url = reverse_lazy('works:list')


class DeleteAlbumView(SuperuserRequiredMixin, DeleteView):
    model = Album
    success_url = reverse_lazy('works:list')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class ChangeAlbumOrderView(SuperuserRequiredMixin, AjaxResponseMixin,
                           JSONResponseMixin, View):

    def get_ajax(self, request, *args, **kwargs):
        ids = [int(id) for id in request.GET['ids'].split(',')]
        ids.reverse()
        for album in Album.objects.in_bulk(ids).values():
            album.index = ids.index(album.id)
            album.save()
        return self.render_json_response({})


class ChangeWorkOrderView(SuperuserRequiredMixin, AjaxResponseMixin,
                          JSONResponseMixin, View):

    def get_ajax(self, request, *args, **kwargs):
        ids = [int(id) for id in request.GET['ids'].split(',')]
        ids.reverse()
        album = Album.objects.get(pk=request.GET['album_id'])
        for work in Work.objects.in_bulk(ids).values():
            work.index = ids.index(work.id)
            work.album = album
            work.save()
        return self.render_json_response({})
