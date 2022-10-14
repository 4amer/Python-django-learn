from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound

def index(request):
    return HttpResponse("Старинца приложжения women")

def categories(request, catid):
    if(catid > 200):
        return redirect("home/", permanent=True)
    return HttpResponse(f"<h1>Статьи по котологам {catid}</h1>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
