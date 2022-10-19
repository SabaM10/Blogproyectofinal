from django import forms

class form_blog(forms.Form):
    titulo = forms.CharField(max_length=30)
    subtitulo = forms.CharField(max_length=30)
    cuerpo = forms.CharField(max_length = 1000)
    autor = forms.CharField(max_length=30)
    fecha = forms.DateField()
    #imagen = forms.ImageField(upload_to='../images')