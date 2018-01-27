from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import (HttpResponse, HttpResponseBadRequest,
                         HttpResponseForbidden) 
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages 
from django.conf import settings as django_settings
from django.core.mail import send_mail

def signup(request):
	print('inside signup_human, authentication.view')     
	if request.method == 'POST':
		email 	 	= request.POST.get('email')
		password 	= request.POST.get('password')
		# full_name   = request.POST.get('full_name')
		exist_user = User.objects.all().filter(username=email)
		exist_email = User.objects.all().filter(email=email)
		if not exist_email or not exist_user:
			print('user does not exists')
			User.objects.create_user(username=email, password=password, email=email) 
			user = authenticate(username=email, password=password)           

			# user.first_name = full_name.split(' ')[0]
			# try:
			# 	user.last_name = full_name.split(' ')[1]
			# except:
			# 	user.last_name = ' ' 
			user.save()
			login(request, user)

			messages.add_message(request,
			                     messages.SUCCESS,
			                     'Hello there start earning now!!'
			                     )
			from_email = django_settings.EMAIL_HOST_USER
			to = [email]
			subject = 'Welcome at profito ' + user.username
			message = 'Dear '+user.username+'!\n'\
					  + ' Happy to see you on Profito\n'\
					  + ' Tell your close ones about the product you love and earn money for this\n'
			# if to:
			#   send_mail(subject,message,from_email,to,fail_silently=False)

			print('inside signup, authentication.views')
			data = 'success'
			return redirect('home')
		else:
			# error = 'True'
			user = authenticate(username=email, password=password)
			login(request, user)
			return redirect('home')
			
	else:
	    return redirect('home')




