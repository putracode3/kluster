"""kluster URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from aplikasi import views as aplikasi_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', aplikasi_views.masukkan),
    url(r'^simpan/', aplikasi_views.simpan),
    url(r'^preproses/', aplikasi_views.preproses),
    url(r'^term/', aplikasi_views.hitung_term),
    url(r'^tf-idf/', aplikasi_views.tf_idf),
]
