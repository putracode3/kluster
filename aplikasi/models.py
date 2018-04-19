# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Kelas(models.Model):
    nama = models.CharField(max_length=100, blank=True)
    objects = models.Manager()
    def __str__(self):
        return self.nama

# Create your models here.
class CrawlDetikNews(models.Model):
    headline = models.TextField(blank=True)
    date = models.CharField(max_length=50) 
    main_headline = models.TextField(blank=True)
    content = models.TextField(blank=True)
    url = models.TextField(blank=True)
    stemming = models.TextField(blank=True)
    stopword = models.TextField(blank=True)
    sum_all_word = models.TextField(blank=True)
    count_term = models.TextField(blank=True)
    kelas = models.ForeignKey(Kelas)
    objects = models.Manager()
    Kelas.objects.get_or_create(nama="lain-lain")[0]

    def __str__(self):
        return self.headline
