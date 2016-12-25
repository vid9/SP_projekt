from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'poraba/registration.html', views.login, name='login'),
	url(r'^$', views.index, name='index'),
]
