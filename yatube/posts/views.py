from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Главная страница')

def group_posts(request):
    return HttpResponse('Группы')

def group_posts(request, any_posts):
    return HttpResponse(f'Группы {any_posts}')
