from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from ..login_reg.models import User
from . import models
from .models import User, Friends
from django.contrib import messages

def index(request):
	return render(request, 'index.html')

def friends(request):
    me = User.objects.get(id=request.session['id'])
    try:
        users = User.objects.all()
        others = []
        for other_user in users:
            if (other_user.id != request.session['id']):
                others.append(other_user)
    except:
        users = None

    try:
        friends = Friend.objects.filter(user_friend=me)
        real_friends = []
        for each_friend in friends:
            real_friends.append(each_friend.second_friend)
        real_others = []
        for other_user in others:
            if (other_user not in real_friends):
                real_others.append(other_user)
    except:
        friends = None

    context = {
        'me' : me,
        'users' : real_others,
        'friends' : real_friends
    }
    return render(request, 'index.html', context)

def myprofile(request, id):
    profile = User.objects.get(id=id)
    context = {
        'user' : profile
    }
    return render(request, 'login/success.html', context)

def profile(request, id):
    profile = User.objects.get(id=id)
    context = {
        'user' : profile
    }
    return render(request, 'index.html', context)

def add_friend(request, id):
    User.userManager.addFriend(request.session['id'], id)
    return redirect('/friends')

def remove_friend(request, id):
    User.userManager.removeFriend(request.session['id'], id)
    return redirect('/friends')

def logout(request):
	if 'user_id' in request.session:
		request.session.pop('user_id')
	return redirect(reverse('main'))