from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from AppProyectoFinal.forms import form_blog
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
    if request.method == 'POST':
        blog = Blog(titulo=request.POST['titulo'], subtitulo = request.POST['subtitulo'],  cuerpo=request.POST['cuerpo'], autor=request.POST['autor'], fecha=request.POST['fecha'])#, imagen = request.POST['imagen']
        blog.save()
        blogs = Blog.objects.all()
        return render(request, 'BlogCRUD/read_blogs.html', {'blogs': blogs})
    return render(request, 'BlogCRUD/create_blogs.html')

def update_blogs(request, blog_id):
    blog = Blog.objects.get(id=blog_id)

    if request.method == 'POST':
        formulario = form_blog(request.POST)

        if formulario.is_valid():
            blog.titulo = request.POST['titulo']
            blog.subtitulo = request.POST['subtitulo']
            blog.cuerpo = request.POST['cuerpo']
            blog.autor = request.POST['autor']
            blog.fecha = request.POST['fecha']
            #blog.imagen = request.POST['imagen']
            blog.save()
            read_blogs()
            blogs = Blog.objects.all()
            return render(request, 'BlogCRUD/read_blogs.html', {'blogs': blogs})
    return render(request, 'BlogCRUD/update_blogs.html', {'blog': blog})

def read_blogs(request = None):
    blogs = Blog.objects.all()
    return render(request, 'BlogCRUD/read_blogs.html', {'blogs': blogs})

def delete_blogs(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    blog.delete()
    blogs = Blog.objects.all()
    return render(request, 'BlogCRUD/read_blogs.html', {'blogs': blogs})

# Path: AppProyectoFinal\urls.py