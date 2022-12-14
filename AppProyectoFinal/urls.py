"""Blogproyectofinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from re import template
from django.urls import path
from Blogproyectofinal.views import *
from django.contrib.auth.views import LogoutView
from AppProyectoFinal.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('About/', about),
    path('Pages/', pages),
    path('Login/', login),
    path('create_blogs/', create_blogs),
    path('update_blogs/<blog_id>', update_blogs),        
    path('read_blogs/', read_blogs),
    path('delete_blogs/<blog_id>', delete_blogs),
]