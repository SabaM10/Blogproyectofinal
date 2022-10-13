from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "index.html")
def about(request):
    return render(request, "about.html")
def pages(request):
    return render(request, "pages.html")
def login(request):
    return render(request, "login.html")
