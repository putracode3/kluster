# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-20 10:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplikasi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='crawldetiknews',
            name='stemming',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='crawldetiknews',
            name='stopword',
            field=models.TextField(blank=True),
        ),
    ]
