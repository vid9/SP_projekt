from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from django.contrib.auth import authenticate, login, logout

from .forms import LoginForm

# Create your views here.

def index(request):
    return render(request, 'porabaapp/index.html')

def userlogin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['uname'], password=form.cleaned_data['psw'])
            if user is not None:
                login(request, user)
                return render(request, 'porabaapp/index.html')
    return render(request, 'porabaapp/login.html')


def register(request):
    return render(request, 'porabaapp/registration.html')

def profil(request):
    return render(request, 'porabaapp/profil.html')

def uporabnik(request):
    return render(request, 'porabaapp/uporabnik.html')

def dodaj(request):
    return render(request, 'porabaapp/dodaj.html')

def logout_user(request):
  logout(request)
  return HttpResponseRedirect(reverse('home'))