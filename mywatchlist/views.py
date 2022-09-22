from django.shortcuts import render
from mywatchlist.models import WatchlistItem
from django.http import HttpResponse
from django.core import serializers

def show_mywatchlist(request):
    data_watchlist = WatchlistItem.objects.all()
    total = len(data_watchlist)
    ditonton = 0
    banyak = False
    for item in data_watchlist:
        if (item.watched):
            ditonton = ditonton + 1
    if (ditonton > (total-ditonton)):
        banyak = True
    context = {
        'watchlist': data_watchlist,
        'nama': 'Daffa Ilham Restupratama',
        'id': '2106751013',
        'banyak': banyak
    }
    return render(request, "mywatchlist.html", context)

def show_html(request):
    data_watchlist = WatchlistItem.objects.all()
    context = {
        'watchlist': data_watchlist,
        'nama': 'Daffa Ilham Restupratama',
        'id': '2106751013'
    }
    return render(request, "watchlist_data.html", context)

def show_xml(request):
    data = WatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = WatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = WatchlistItem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = WatchlistItem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")