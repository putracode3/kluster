# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

import json
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
    # create stemmer
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    # stemming process
    sentence = 'Surabaya - Dinas Perhubungan (dishub) Surabaya mengimbau pengguna jalan untuk menghindari Jalan Kartini yang ditutup karena jembatannya ambles. Pengguna jalan diimbau untuk mencari jalan lain atau jalan alternatif. \"Kami mengimbau kepada para pengguna jalan agar mencari alternatif jalur lain di saat jam aktif. Dikhawatikan akan terjadi kemacetan,\" kata Kabid Lalu Lintas Dinas Pergubungan Kota Surabaya Rubben Rico kepada detikcom, Senin (12/3/2018).Ruben mengatakan pihaknya sudah melakukan rekayasa pengalihan arus sejak hari Minggu (12/3/2018). \"Kami alihkan yang dari Jalan Darmo bisa melewati WR Supratman atau melewati Jalan rr Soetomo. Sebaliknya dari Banyu Urip atau dari Diponegoro bisa lewat Jalan Padegiling atau lewat dr Soetomo,\" ujar Rubben.Rubben mengatakan penutupan sebagian Jalan Kartini akan berlangsung sekitar 6 hari. \"Kami mendapatkan info dari Dinas PU bahwa jembatan ini akan ditutup selama 6 hari. Karena mereka meminta waktu yang cukup. Sebab salah satu girder Jembatan Kartini ada yang patah. Jadi perlu pemancangan,\" kata Ruben.Dalam pantauan detikcom, perempatan Jalan Kartini yang mengarah ke Jalan Diponegoro ditutup dengan mengunakan barrier. Selain itu, warga yang penasaran berdatangan melihat amblesnya jalan rusak. (iwd/iwd) jembatan kartini ambles pemkot surabaya dinas pu surabaya dishub surabaya'
    output   = stemmer.stem(sentence)

    # ------------------- Stopword Removal
    # factory = StopWordRemoverFactory()
    # stopword = factory.create_stop_word_remover()
    # Kalimat
    # kalimat = 'Dengan Menggunakan Python dan Library Sastrawi saya dapat melakukan proses Stopword Removal'
    # stop = stopword.remove(kalimat)

    fa = StopWordRemoverFactory()
    stopword = fa.create_stop_word_remover()
    kalimat = output
    stop = stopword.remove(kalimat)
    stop = stop.replace(' - ', ' ')
    output = stop

    return render(request, 'beranda/preprocessing.html', {"rootword": output, "ori":sentence})