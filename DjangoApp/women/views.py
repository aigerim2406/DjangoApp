from django.http import HttpResponse
from django.shortcuts import render

def index(request): #HttpRequest
    return HttpResponse("Главная страница")

def categories(request, catid):
    return HttpResponse(f"<h1>Аксессуар по категориям</h1><p>{catid}</p>")
def not_found(request,exception):
    return HttpResponse("<h1>Страница не найдена</h1>")