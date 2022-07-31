"""Nutrimec URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from core.forms import loginForm, UserRegisterForm
from core.views import *
from core import views as core_views
from django.contrib.auth import  views as auth_views

urlpatterns = [
    path('', core_views.index, name="index" ),
<<<<<<< HEAD
    path('register/', register.as_view(), name="register" ),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name = 'core/login.html',authentication_form=loginForm), name="login" ),
    path('logout/', auth_views.LogoutView.as_view(template_name='core/logout.html'), name='logout'),
=======
    path('register/', core_views.register, name="register" ),
    path('login/', core_views.login, name="login" ),
>>>>>>> e0924aaadd4ed381d5d40b141962fb549de65f9a
    path('contact/', core_views.contact, name="contact" ),
    path('nosotros/', core_views.nosotros, name="nosotros" ),
    path('recetas/', core_views.recetas, name="recetas" ),
    path('admin/', admin.site.urls),
]
