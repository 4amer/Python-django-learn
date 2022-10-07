from django.shortcuts import render
from django.http import HttpResponse 

def index(request):
    return HttpResponse("Старинца приложжения women")

def categories(request):
    return HttpResponse("<h1>Статьи по котологам</h1>")
