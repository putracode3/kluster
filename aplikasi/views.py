# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render



# Create your views here.
def masukkan(request):
    return render(request, 'beranda/index.html')