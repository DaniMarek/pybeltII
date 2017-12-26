from django.conf.urls import url 
from . import views

urlpatterns=[
	url(r'^$', views.index, name='main'),
	url(r'^success$', views.success, name='successpg'),
	url(r'^registration$', views.registration, name='registration'),
	url(r'^login$', views.login, name='login'),
	url(r'^logout$', views.logout, name='logout'),
]