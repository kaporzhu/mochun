# -*- coding: utf-8 -*-
from django.db import models

from easy_thumbnails.fields import ThumbnailerImageField


class Album(models.Model):
    name = models.CharField(u'名字', max_length=64)
    icon = ThumbnailerImageField(u'图标', upload_to='album')
    index = models.IntegerField(db_index=True)
    visible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

    @property
    def works(self):
        return self.work_set.all().order_by('-index')

    @property
    def visible_works(self):
        return self.work_set.filter(visible=True).order_by('-index')


class Work(models.Model):
    album = models.ForeignKey(Album, verbose_name=u'专辑')
    image = ThumbnailerImageField(u'画', upload_to='work')
    visible = models.BooleanField(default=True)
    description = models.TextField(u'描述')
    index = models.IntegerField(db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
