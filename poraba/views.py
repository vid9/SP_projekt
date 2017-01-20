from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required, permission_required
from django.core import serializers
from django.shortcuts import render_to_response
from django.template.context import RequestContext

import json

from .forms import LoginForm, RegistrationForm, SpecifikacijeForm, PorabaForm
from .models import Car, Specifikacije, Znamka,  UserCar


# Create your views here.




def ajax_car_search(request):
    if request.is_ajax():
        id = Znamka.objects.get(znamka=request.POST['car'])        #results = Car.objects.values("ime")

        #data = serializers.serialize('json', Car.objects.get("model").filter(znamka=id), fields=("model"))
        data = list(Car.objects.values('model').filter(znamka=id))
        print(data)
        return render_to_response("index.html", {"avto": data})
        #return render(request,"index.html", {"avto": data})

def index(request):
    context = {}
    # context['znamka'] = Car.objects.values("znamka").distinct()
    context['znamka'] = Znamka.objects.values("znamka").distinct()
    context['model'] = Car.objects.values("model").distinct()
    print(context['znamka'])
    if request.is_ajax():
        ajax_car_search(request)
    #context['avto'] = Car.objects.values("model").distinct()
    #print(context['avto'], "test")
    #del context['avto']
    return render(request, 'index.html', context)


def userlogin(request):
    form = LoginForm()
    context = {"loginForm": form}
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/poraba')
                #  context['username'] = user
                # context['username'] = form.cleaned_data['username']
    else:
        form = LoginForm()
        context['LoginForm'] = form
    return render(request, "login.html", context)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password'])
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()
            return HttpResponseRedirect('/poraba')
        else:
            raise ValidationError("User was not created!")
    else:
        form = RegistrationForm()
        context = {"registrationForm": form}
    return render(request, 'registration.html', context)

@login_required(login_url='/login/')
def profil(request):
    context = {}
    form = PorabaForm()
    context['porabaForm'] = form
    if request.method == 'POST':
        form = PorabaForm(request.POST)
        if form.is_valid():
            a = Car.objects.get(id=form.cleaned_data['avto'])
            temp = Specifikacije.objects.values("visina").filter(ime=a)
            context["visina"] = temp[0]["visina"]
            temp = Specifikacije.objects.values("dolzina").filter(ime=a)
            context["dolzina"] = temp[0]["dolzina"]
            temp = Specifikacije.objects.values("tip").filter(ime=a)
            if temp[0]["tip"]:
                context["tip"] = "Dizel"
            else:
                context["tip"] = "Bencin"
            temp = Specifikacije.objects.values("vtanka").filter(ime=a)
            context["tank"] = temp[0]["vtanka"]
            p = UserCar.objects.values("poraba").filter(ime=a, user=request.user)
            s = 0
            for m in range(len(p)):
                print(p[m]['poraba'])
                s += p[m]['poraba']
            s = (s+form.cleaned_data['poraba'])/(len(p)+1)
            context['tr_poraba'] = s
            render(request, 'profil.html', context)
        else:
            print(form.errors)

    else:
        form = PorabaForm()
        context['porabaForm'] = form
    return render(request, 'profil.html', context)

@login_required(login_url='/login/')
def uporabnik(request):
    return render(request, 'uporabnik.html')

@login_required(login_url='/login/')
@permission_required('add_car', raise_exception=True)
def dodaj(request):
    form = SpecifikacijeForm()
    context = {"specifikacijeForm": form}
    if request.method == 'POST':
        print("sent")
        form = SpecifikacijeForm(request.POST)
        if form.is_valid():
            print("valid")
            znamka, _ = Znamka.objects.get_or_create(znamka=form.cleaned_data['znamka'])
            serija, _ = Serija.objects.get_or_create(znamka=znamka, serija=form.cleaned_data['serija'])
            avto, _ = Car.objects.get_or_create(znamka=znamka, serija=serija, model = form.cleaned_data['model'])
            specifikacije = Specifikacije.objects.create(visina = form.cleaned_data['visina'],
                                                         dolzina = form.cleaned_data['dolzina'],
                                                         tip = form.cleaned_data['tip'],
                                                         vtanka = form.cleaned_data['vtanka'],
                                                         ime = avto)
            return HttpResponseRedirect('/poraba')
        else:
            print(form.errors)

    else:
        form = SpecifikacijeForm()
        context['SpecifikacijeForm'] = form
    return render(request, 'dodaj.html', context)

def logout_user(request):
  logout(request)
  return HttpResponseRedirect(reverse('poraba'))