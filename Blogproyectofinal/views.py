from multiprocessing import AuthenticationError
from nturl2path import url2pathname
from django.shortcuts import render

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth. import login, logout, Authenticate

# Create your views here.
def home(request):
    return render(request, "index.html")
def about(request):
    return render(request, "about.html")
def pages(request):
    return render(request, "pages.html")
def login(request):
    return render(request, "login.html")

###################login, registro users y modificacion users #####3

def login_request (request):
    if request.method == "POST":
        form = AuthenticationForm (request, data =request.POST)

        if form.is_valid():
            user = form.cleaned_data.get ('username')
            pwd = form.cleaned_data.get ('password')

            user = authenticate(username = user, password = pwd)

            if user is not None:
                login (request, user)
                avatar = Avatar.objects.filter (user = request.user.id)
                try:
                    avatar = avatar [0].image.url
                except:
                    avatar = None
                            
                return render (request, "index.html", {"avatar" :avatar})
      
            else:
                return render (request, "login.html", {"form" :form})  
        else: 
            return render (request, "login.html", {"form" : form}) 

form = AuthenticationForm ()
return render (request. "login.html", {'form': form})
            
def registro(request):
    if request.method == "POST":
        form = UserRegisterForm (request.POST)
        if form.is_valid():
            #username = form.cleaned_data('username)
            form.save()
            return redirect("login/")
        else:
            return render (request, "registro.html", {'form':form})
    form = UserRegisterForm()
    return render (request, "registro.html", {'form':form})

@login_required

def editarPerfil (request):
    usuario = request.user
    user_basic_info = User.objects.get(id =usuario.id)
    if request.method =='POST':
        form = UserEditForm (request.POST, instance = usuario)
        if form. is_valid ():
             user_basic_info.username = form.cleaned_data.get ('username')
             user_basic_info.email = form.cleaned_data.get ('email')
             user_basic_info.save()
             avatar = Avatar.objects.filter (user = request.user.id)
             try:
                avatar = avatar [0].image.url
             except:
                avatar = None
             return render (request, "index.html", {'avatar': avatar})
        else;
             return render (request, "editarPerfil.html", {'form': form)
    else:
        form = UserEditForm (initial = {'username': usuario.username, 'email': usuario.email})
    return render (request, "editarPerfil.html", {'form': form, 'usuario': usuario})
                 })          
def changePass (request):
    usuario = request.user
    if request.method =="POST":
       
        if form.is_valid():
            user = form.save()
            update_session_auth_hash (request, user)
            avatar = Avatar.objects.filter (user = request.user.id)
            try:
                avatar = avatar [0].image.url
            except:
                avatar = None
            return render (request, "index.html", {"avatar" :avatar})   
    else:
         form = ChangePasswordForm (user =request.user)
    return render (request, "changepass.html", {'form': form, "usuario": usuario})
    
    
################# funcion avatar#####################
               ]
@login_required

def AgregarAvatar (request):
    if request.method =='POST':
        form = AvatarFormulario (request.POST, request.FILES)
        if form.is_valid():
            user = User.objects.get (username = request.user)
            avatar = Avatar (user = user, image = form.cleaned_data['avatar'], id = request.user.id())
            avatar.save()
            avatar = Avatar.objects.filter (user = request.user.id)
            try:
                avatar = avatar [0].image.url
            except:
                avatar = None
            return render (request, "index.html", {'avatar': avatar})
    else:
        try:
             avatar = Avatar.objects.filter (user = request.user.id)  
             form = AvatarFormulario ()
    return render (request, "AgregarAvatar.html", ['form': form])     

