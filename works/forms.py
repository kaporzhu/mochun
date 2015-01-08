# -*- coding: utf-8 -*-
from django import forms

from .models import Work, Album


class WorkForm(forms.ModelForm):

    class Meta:
        model = Work
        fields = ('image', 'description')


class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ('icon', 'name')
