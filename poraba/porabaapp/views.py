from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse


# Create your views here.


def hello(request):
    name = "Vid"
    html = "<HTML><body>Hi %s, thus seems to work!</body></html>" % name
    return HttpResponse(html)

def index(request):
    return render(request, 'porabaapp/index.html')

def login(request):
    return render(request, 'porabaapp/registration.html')