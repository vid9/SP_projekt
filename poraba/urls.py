from django.conf.urls import url, include
from .views import ajax_car_search

from . import views

"""
urlpatterns = [

    url(r'register.html', views.register, name='register'),
    url(r'login.html', views.userlogin, name='login'),
    url(r'dodaj.html', views.dodaj, name='dodaj'),
    url(r'profil.html', views.profil, name='profil'),
    url(r'uporabnik.html', views.uporabnik, name='uporabnik'),
    url(r'index.html', views.index, name='home'),
    url(r'^logout', views.logout_user, name='logout'),
    url(r'^$', views.index),
    ,
    url(r'^car/$', ajax_car_search, name='demo_car_search'),
]
"""