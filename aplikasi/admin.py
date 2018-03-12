# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from aplikasi.models import *

# Register your models here.
class CrawlDetikNewsAdmin(admin.ModelAdmin):
    list_display = ['headline', 'date', 'main_headline', 'content', 'url']
    list_filter = ('headline', 'date', 'main_headline', 'content', 'url')
    search_fields = ['headline', 'date', 'main_headline', 'content', 'url']
    list_per_page = 25
admin.site.register(CrawlDetikNews, CrawlDetikNewsAdmin)