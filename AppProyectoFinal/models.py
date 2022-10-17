from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Blog(models.Model):
    titulo = models.CharField(max_length=30)
    subtitulo = models.CharField(max_length=30)
    cuerpo = models.CharField(max_length = 1000)
    autor = models.CharField(max_length=30)
    fecha = models.DateField()
    imagen = models.ImageField(upload_to='images/')
    def __str__(self):
        return f"Titulo: {self.titulo} - Subtitulo:{self.subtitulo} - Cuerpo: {self.cuerpo} - Autor: {self.autor} - Fecha: {self.fecha} - Imagen: {self.imagen}"