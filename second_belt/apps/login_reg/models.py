from __future__ import unicode_literals
from django.db import models
import re
import bcrypt

# EMAIL_REGEX=re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
# NAME_REGEX=re.compile(r'^[A-Za-z]\w+$')

class UserManager(models.Manager):
	def validate_registration(self, postData):
		errors=[]
		if len(postData['fname'])<2:
			errors.append('First Name should be more than 2 characters')
		if len(postData['lname'])<2:
			errors.append('Last Name should be more than 2 characters')
		if len(postData['email'])==0:
			errors.append('Invalid email')
		# Below code to use email REGEX	
		# if not re.match(EMAIL_REGEX, postData['email']):
		# 	errors.append('Invalid email')

		if len(postData['password'])<2:
			errors.append('Password should be more than 2 characters.')
		if postData['password'] != postData['password_confirmation']:
			errors.append('Passwords must match! Retype or whatever, but like carefully')
		return errors

	def validate_login(self, postData):
		errors=[]
		# Email
		if len(postData['email'])==0:
			errors.append('Invalid email')
		# Password
		if len(postData['password'])==0:
			errors.append('Password is required')

		if len(errors): 
			return {'errors':errors}


		user = User.objects.filter(email=postData['email']).first()
		
		if user:
			user_password= postData['password'].encode()
			db_password= user.password.encode()
			# print user_password, '-------------------'
			# print db_password
			if bcrypt.checkpw(user_password, db_password):
				return {'user':user}
		
		return {'errors':errors}
	
	def create_user(self, postData):
		hashedpw=bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
		return User.objects.create(
			fname=postData['fname'],
			lname=postData['lname'],
			email=postData['email'],
			password=hashedpw,
			)

class User(models.Model):
	fname=models.CharField(max_length=255)
	lname=models.CharField(max_length=255)
	email=models.CharField(max_length=255)
	password=models.CharField(max_length=255)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)

	objects=UserManager()

	def __unicode__(self):
		return 'fname:{}, lname:{}, email:{}, password:{}, id:{}'.format(self.fname, self.lname, self.email, self.password, self.id)

