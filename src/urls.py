"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from poraba.views import register, index, userlogin, dodaj, profil, uporabnik, logout_user, ajax_car_search

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register/$', register, name='register'),
    url(r'^login/$', userlogin, name='login'),
    url(r'^add/$', dodaj, name='add'),
    url(r'^profile/$', profil, name='profil'),
    url(r'^search/$', uporabnik, name='search'),
    url(r'^poraba/$', index, name='poraba'),
    url(r'^logout/$', logout_user, name='logout'),
    url(r'', index, name='home'),
    url(r'^car/$', ajax_car_search, name='demo_car_search'),
]
