from tokenize import Floatnumber
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from AppProyectoFinal.forms import *
from .models import Blog

#para el login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
#import datetime
from datetime import datetime

#decorador para que solo se pueda acceder a la pagina si estas logeado
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return render(request, 'index.html', {"mensaje": f"Bienvenido {username}"} )
            else:
                return render(request, 'login.html', {"mensaje": "Usuario o contraseña incorrectos"})
    else:
                return render(request, 'login.html', {"mensaje": "Formulario errroneo!"})
    form = AuthenticationForm()

    return render(request, 'login.html', {"form": form})

def register(request):

    if request.method == 'POST':

        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            return render(request, 'index.html', {"mensaje": f"Bienvenido {username}"} )
    else:
        form = UserRegisterForm()
    
    return render(request, 'registro.html', {"form": form})


@login_required
def index(request):
    return render(request, 'index.html')
@login_required
def about(request):
    return render(request, 'about.html')
@login_required
def pages(request):
    return render(request, 'pages.html')

@login_required
def editarPerfil(request):
    usuario = request.user

    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password1']
            usuario.save()
            return render(request, 'index.html', {"mensaje": f"Perfil editado correctamente"})
    else:
        miFormulario = UserEditForm(initial = {'email': usuario.email})

    return render(request, 'editarPerfil.html', {'miFormulario': miFormulario, 'usuario': usuario})

def create_blogs(request):
    blog = Blog()
    if request.method == 'POST':
        
        formulario = form_blog(request.POST, request.FILES)
        if formulario.is_valid():
            blog.titulo = request.POST['titulo']
            blog.subtitulo = request.POST['subtitulo']
            blog.cuerpo = request.POST['cuerpo']
            blog.autor = request.POST['autor']
            #get a date from a form and convert it to a datetime object
            blog.fecha = datetime.strptime(request.POST['fecha'], '%Y-%m-%d')
            #get a image from a form and convert it to a image object
            blog.imagen = request.FILES['imagen']
            blog.save()
            blogs = Blog.objects.all()
        return render(request, 'BlogCRUD/read_blogs.html', {'blogs': blogs})
    return render(request, 'BlogCRUD/create_blogs.html')

def read_blogs(request = None):
    blogs = Blog.objects.all()
    return render(request, 'BlogCRUD/read_blogs.html', {'blogs': blogs})

def update_blogs(request, blog_id):
    blog = Blog.objects.get(id=blog_id)

    if request.method == 'POST':
        formulario = form_blog(request.POST)

        if formulario.is_valid():
            blog.titulo = request.POST['titulo']
            blog.subtitulo = request.POST['subtitulo']
            blog.cuerpo = request.POST['cuerpo']
            blog.autor = request.POST['autor']
            #get a date from a form and convert it to a datetime object
            blog.fecha = datetime.strptime(request.POST['fecha'], '%Y-%m-%d')
            #get a image from a form and convert it to a image object
            blog.imagen = request.FILES['imagen']
           # blog.imagen = request.POST['imagen']
            blog.save()
            read_blogs()
            blogs = Blog.objects.all()
            return render(request, 'BlogCRUD/read_blogs.html', {'blogs': blogs})
    else:
        formulario = form_blog(initial = {'titulo': blog.titulo, 'subtitulo': blog.subtitulo, 'cuerpo': blog.cuerpo, 'autor': blog.autor, 'fecha': blog.fecha, 'imagen': blog.imagen})
    return render(request, 'BlogCRUD/update_blogs.html', {'blog': blog})

def delete_blogs(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    blog.delete()
    blogs = Blog.objects.all()
    return render(request, 'BlogCRUD/read_blogs.html', {'blogs': blogs})

# Path: AppProyectoFinal\urls.py