from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404


def bruh(requare):
    return HttpResponse("<h1>Bruh</h1>");

def into(requare, Br):
    if(requare.GET):
        print(requare.GET)
    if(Br > 5000):
        raise Http404();
    return HttpResponse(f"<h1>Вот результат {Br}</h1>");

def intoger(request, exception):
    return HttpResponseNotFound("<h1>Not found</h1>");
