from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Blog

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def pages(request):
    return render(request, 'pages.html')

def login(request):
    return render(request, 'login.html')

def create_blogs(request):
    return render(request, 'create_blogs.html')

def update_blogs(request, blog_id):
    return render(request, 'update_blogs.html')

def read_blogs(request = None):
    blogs = Blog.objects.all()
    return render(request, 'read_blogs.html', {'blogs': blogs})

def delete_blogs(request, blog_id):
    return render(request, 'delete_blogs.html')

# Path: AppProyectoFinal\urls.py