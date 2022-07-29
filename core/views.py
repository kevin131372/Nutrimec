from django.contrib import messages
from multiprocessing import context
from tkinter.tix import Form
from urllib import response
from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register (request):
    if request.method =='POST':
        new_nombres = request.POST.get('name','')
        new_apellidos = request.POST.get("lastname",'')
        new_correo = request.POST.get("correo",'')
        new_password = request.POST.get("password",'')
        user = User(nombres=new_nombres,apellidos=new_apellidos,correo=new_correo,password=new_password)
        user.save()
        return redirect('recetas')
    else:
        User()
    return render(request, 'core/register.html')

def login (request):
    return render(request, 'core/login.html')

def index (request):
    return render(request, 'core/index.html')

def contact (request):
    return render(request, 'core/contact.html')
    
def nosotros (request):
    return render(request, 'core/nosotros.html')

def recetas (request):
    return render(request, 'core/recetas.html')



