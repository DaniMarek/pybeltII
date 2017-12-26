from django.shortcuts import render, HttpResponse, redirect, reverse
from . import models
from .models import User
from django.contrib import messages

def flash_errors(errors, request):
	for error in errors:
		messages.error(request, error)

def current_user(request):
	return User.objects.get(id=request.session['user_id'])

def index(request):
	
	return render(request, 'login/index.html')

def success(request):
	if 'user_id' in request.session:
		context={
			'user':current_user(request)
		}
		return render(request, 'login/success.html', context )
	return redirect(reverse('main'))

def registration(request):
	if request.method=='POST':
		# Validate form data
		errors=User.objects.validate_registration(request.POST)
		# Check if errors don't exist
		if not errors:
			# Create user
			user= User.objects.create_user(request.POST)
			# login the user
			request.session['user_id']=user.id
			# redirect to success page
			return redirect(reverse('successpg'))
		# flash errors
		flash_errors(errors, request)

	return redirect(reverse('main'))
	# User.objects.create(
	# 	first_name=request.POST['first_name'],
	# 	last_name=request.POST['last_name'],
	# 	email=request.POST['email'],
	# 	password=request.POST['password']		
	# 	)

def login(request):
	if request.method=='POST':
		# Validate my login data
		check=User.objects.validate_login(request.POST)
		# Check if retrieved a valid user
		if 'user' in check:
			#Log in user
			print check
			request.session['user_id']=check['user'].id
			#Redierct to success page
			return redirect(reverse('successpg'))
		# Flash error messages
		flash_errors(check['errors'], request)
			
	return redirect(reverse('main'))

def logout(request):
	if 'user_id' in request.session:
		request.session.pop('user_id')
	return redirect(reverse('main'))