# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CrawlDetikNews(models.Model):
    headline = models.TextField(blank=True)
    date = models.CharField(max_length=50) 
    main_headline = models.TextField(blank=True)
    content = models.TextField(blank=True)
    url = models.TextField(blank=True)
    stemming = models.TextField(blank=True)
    stopword = models.TextField(blank=True)
    objects = models.Manager()

    def __str__(self):
        return self.headline
