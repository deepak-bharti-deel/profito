import json     
import time, datetime 
from django.contrib.auth.models import User 
from os.path import splitext, basename
from django.db.models import Q 
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import (HttpResponse, HttpResponseBadRequest,
                         HttpResponseForbidden)  
from django.shortcuts import get_object_or_404, render, redirect
# from django.core.urlresolvers import reverse
from django.http import JsonResponse   
from django.template.context_processors import csrf  
from django.template.loader import render_to_string     
  
# from profito.decorators import ajax_required    
from Feeds.models import Feed      
from Feeds.forms import FeedForm   
from Users.models import Profile   
from PIL import Image, ImageFile 
from Users.models import Profile
from django.core.mail import send_mail
from django.conf import settings as django_settings
import random


# @login_required
def ads(request): #post with images and require page refresh
    user = request.user
    if request.method=="POST":
	    form = FeedForm(request.POST or None, request.FILES or None)
	    if form.is_valid():
	        instance = form.save(commit=False)
	        post   = request.POST['post']
	        amount = request.POST.get('amount')	        
	        post = post.strip()     	#+ str(to_user_profile_pk_indirect)
	        if len(post) > 0:
	            instance.post = post[:255]
	            instance.amount = amount
	            instance.save()  
	            feed=instance
	            # instance.optimize_image()
    ads = Feed.objects.all()
    return render(request, 'feeds/ads.html', {'ads':ads})


def ad_detail(request, id=id):
	ad = get_object_or_404(Feed, id=id)
	return render(request, 'feeds/ad_detail.html', {'ad':ad})

