from django.shortcuts import render
from django.http import HttpResponse

def native(request):
    return HttpResponse("<h3>Hm... women... Hahahahahahahahah</h3>")

def bruh(request):
    return HttpResponse("Bruh Bruh Bruh Bruh Bruh Bruh Bruh")