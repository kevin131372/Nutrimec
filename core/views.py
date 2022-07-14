from email import message
from multiprocessing import context
from tkinter.tix import Form
from urllib import response
from django.shortcuts import render, HttpResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register (request):   
    new_nombres = request.POST.get('name','')
    new_apellidos = request.POST.get("lastname",'') 
    new_correo = request.POST.get("correo",'') 
    new_password = request.POST.get("password",'') 
    user = User(nombres=new_nombres,apellidos=new_apellidos,correo=new_correo,password=new_password)
    user.save()
    return render(request, 'core/register.html')

def index (request):
    return render(request, 'core/index.html')



