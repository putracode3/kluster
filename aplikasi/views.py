# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

import json,ast
from aplikasi.models import CrawlDetikNews

from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory


# Create your views here.
def masukkan(request):
    return render(request, 'beranda/index.html')


def simpan(request):
    json_data = open('assets/detik.json')
    baca_file = json.load(json_data)
    # baca_file = json.dumps(json_data) // json formatted string

    # json.dumps(json_data)

    for p in baca_file:
        headline = p['headline']
        main_headline = p['main_headline']
        date = p['date']
        url = p['url']
        content = p['content']

        # save if not exist data
        CrawlDetikNews.objects.get_or_create(
            headline=headline,
            main_headline=main_headline,
            date=date,
            url=url,
            content=content
        )

    json_data.close()
    baca_db = CrawlDetikNews.objects.all().order_by('-id')

    return render(request, 'beranda/simpan.html', {"baca_json": baca_db})


def preproses(request):
    baca_db = CrawlDetikNews.objects.all()
    kounter = 0
    for baca in baca_db:
        kounter += 1
        if kounter > 325 and kounter <= 475:
            # create stemmer
            factory = StemmerFactory()
            stemmer = factory.create_stemmer()
            # stemming process
            sentence = baca.headline +" "+ baca.content
            output = stemmer.stem(sentence)
            baca.stemming = output

            # ------------------- Stopword Removal
            fa = StopWordRemoverFactory()
            stopword = fa.create_stop_word_remover()
            kalimat = output
            stop = stopword.remove(kalimat)
            stop = stop.replace(' - ', ' ')
            output = stop
            baca.stopword = output

            baca.save()

    return render(request, 'beranda/preprocessing.html', {"rootword": "output", "ori": sentence})

def hitung_term(request):
    baca_db = CrawlDetikNews.objects.all()
    kounter = 0
    for baca in baca_db:
        kounter += 1
        if kounter > 325 and kounter <= 400:
            counts = dict()
            # get from db >> stopword
            str_db = baca.stopword
            words = str_db.split()
            for word in words:
                if word in counts:
                    counts[word] += 1
                else:
                    counts[word] = 1
            baca.count_term = ast.literal_eval(json.dumps(counts))
            baca.sum_all_word = len(words)
            baca.save()

    return render(request, 'beranda/term.html', {'priview':ast.literal_eval(json.dumps(counts))})

def tf_idf(request):
    return render(request, 'beranda/tf_idf.html')
