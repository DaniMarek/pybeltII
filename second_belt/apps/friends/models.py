from __future__ import unicode_literals
from django.contrib.auth.models import User
from ..login_reg.models import User
from django.db import models

class Action(models.Manager):
	
	def Add(self, user_id, friend_id):
		user=self.get(id=user_id)
		friend=self.get(id=friend_id)
		Friend.objects.create(user_friend=user, other_friend=friend)
		Friend.objects.create(user_friend=friend, other_friend=user)

		return User.objects.create(
			alias=postData['alias'],
			name=postData['name'],
			email=postData['email'],
			)

	def Delete(self, user_id, friend_id):
		user=self.get(id=user_id)
		friend=self.get(id=friend_id)
		friendship1=Friend.objects.get(user_friend=user, other_friend=friend)
		friendship2=Friend.objects.get(user_friend=friend, other_friend=user)
		friendship1.delete()
		friendship2.delete()

class Friends(models.Model):
	user_friend=models.ForeignKey(User, related_name="friend_request")
	second_friend=models.ForeignKey(User, related_name="friend_accept")
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)

	objects=models.Manager()

