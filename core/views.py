from django.contrib import messages
from multiprocessing import context
from tkinter.tix import Form
from urllib import response
from django.shortcuts import render, HttpResponse, redirect
from .models import *
from .forms import loginForm, UserRegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.contrib.auth.views import LoginView

# Create your views here.
class register(View):
  form_class = UserRegisterForm
  initial = {'key': 'value'}
  template_name = 'core/register.html'

  def get(self, request, *args, **kwargs):
    form = self.form_class(initial=self.initial)
    return render(request, self.template_name, {'form': form})

  def post(self, request, *args, **kwargs): 
    form = self.form_class(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        messages.success(request, f'Account created for {username}')
        return redirect(to='/')
    return render(request, self.template_name, {'form': form})
  def dispatch(self, request, *args, **kwargs):
    # will redirect to the home page if a user tries to access the register page while logged in
    if request.user.is_authenticated:
        return redirect(to='/')
    # else process dispatch as it otherwise normally would
    return super(register, self).dispatch(request, *args, **kwargs)

class CustomLoginView(LoginView):
    form_class = loginForm
    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')
        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)
            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True
        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)

def login (request):
    return render(request, 'core/login.html')

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



