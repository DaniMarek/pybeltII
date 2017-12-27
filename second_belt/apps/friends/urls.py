from django.conf.urls import url 
from . import views

urlpatterns=[
	url(r'^$', views.index, name='main'),
	url(r'^myprofile$', views.myprofile, name='myprofile'),
	url(r'^profile$', views.profile, name='profile'),
	url(r'^logout$', views.logout, name='logout'),
]