from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound

from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]

def index(request):
    
    return render(request, 'women/index.html', {'menu': menu, 'title': 'Главная страница'})

def about(request):
    posts = Women.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'О сайте'
    }
    return render(request, 'women/about.html', context=context)

def addpage(request):
    return HttpResponse("Добавление статьи")

def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")

def show_post(request, post_id):
    return HttpResponse(f"Отоброжение статьи с id = {post_id}")

def categories(request, catid):
    if(catid > 200):
        return redirect("home/", permanent=True)
    return HttpResponse(f"<h1>Статьи по котологам {catid}</h1>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
