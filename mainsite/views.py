from django.shortcuts import render
from .models import News


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'service.html')

def news(request):
    new_list = News.objects.all()
    context = {
       'new_list':new_list
    }
    return render(request, 'blog.html', context)

def contact(request):
    return render(request, 'contact.html')