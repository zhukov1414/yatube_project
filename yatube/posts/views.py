from django.http import HttpResponse
from django.shortcuts import render
from .models import Post


def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    title = '"Это главная страница проекта Yatube"'
    context = {
        'title':title,
        'posts': posts, 
    }
    return render(request, 'posts/index.html', context)


def group_list(request, slug):
    template_post = 'posts/group_list.html'
    title = "Здесь будет информация о группах проекта Yatube"
    context = {
        'title': title, 
    }
    return render(request, template_post, context)

