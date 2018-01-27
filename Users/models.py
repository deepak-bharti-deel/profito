import hashlib 
import os.path 
import urllib   
     
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models 
from django.db.models.signals import post_save 
from django.core.cache import cache 
import datetime
from django.contrib.auth import authenticate, login

  
class Profile(models.Model):     
    user = models.OneToOneField(User, on_delete='models.cascade')  

    is_product = models.BooleanField(default=False)
    company = models.CharField(max_length=100, null=True, blank=True)
    facebook = models.CharField(max_length=150, null=True, blank=True)
    quora = models.CharField(max_length=150, null=True, blank=True)
    twitter = models.CharField(max_length=150, null=True, blank=True)
    linkedin = models.CharField(max_length=150, null=True, blank=True)

    home = models.CharField(max_length=100, null=True, blank=True)
    website = models.CharField(max_length=100, null=True, blank=True)
    job = models.CharField(verbose_name="what are you doing now?", max_length=100, null=True, blank=True) 
    
    
    gender = models.CharField(max_length=10, null=True, blank=True)
    image = models.ImageField(upload_to='profile_pictures',
                                # format='JPEG',
                                # options={ 'quality': 100},
                                null=True,
                                blank=True,
            height_field="height_field",
            width_field="width_field")
    height_field = models.IntegerField(default=450)
    width_field = models.IntegerField(default=350)
    shares = models.IntegerField(default=100,blank=True, null=True)
    profitos = models.IntegerField(default=100,blank=True, null=True)

    class Meta: 
        db_table = 'users_profile'

    def __str__(self):
        return self.user.username

    def website(self):
        url = self.website
        if "http://" not in self.website and "https://" not in self.website and len(self.website) > 0:  # noqa: E501
            url = "http://" + str(self.website)
        return url

    def facebook(self):
        url = self.facebook
        if "http://" not in self.facebook and "https://" not in self.facebook and len(self.facebook) > 0:  # noqa: E501
            url = "http://" + str(self.facebook)
        return url

    def quora(self):
        url = self.quora
        if "http://" not in self.quora and "https://" not in self.quora and len(self.quora) > 0:  # noqa: E501
            url = "http://" + str(self.quora)
        return url

    def twitter(self):
        url = self.twitter
        if "http://" not in self.twitter and "https://" not in self.website and len(self.twitter) > 0:  # noqa: E501
            url = "http://" + str(self.twitter)
        return url

    def linkedin(self):
        url = self.linkedin
        if "http://" not in self.linkedin and "https://" not in self.linkedin and len(self.linkedin) > 0:  # noqa: E501
            url = "http://" + str(self.linkedin)
        return url

    def get_picture(self):
        #print('settings.MEDIA_URL,self.image',settings.MEDIA_URL,self.image)
        no_picture = settings.MEDIA_URL + 'profile_pictures/' + 'no_picture.png'
        gender = self.gender
        if self.image:
            return settings.MEDIA_URL+str(self.image)
        elif gender:
            if gender.lower() == 'male':
                return settings.MEDIA_URL + 'profile_pictures/' + 'male.png'
            elif gender.lower() == 'female': 
                return settings.MEDIA_URL + 'profile_pictures/' + 'female.png'
            elif gender == 'Gender':
                return no_picture
        else:
            return no_picture

    def get_screen_name(self): 
        try:
            if self.user.get_full_name():
                return self.user.get_full_name()
            else:
                return self.user.username
        except:
            return self.user.username



def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


def save_user_profile(sender, instance, **kwargs):  
    instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)



   




       # def unotify_wrote_on_profile(self,profile,feed):
    #     if self.user!= profile.user:
    #         Notification.objects.filter(notification_type=Notification.WROTE_ON_PROFILE,
    #                      from_user=self.user, to_user=profile.user,
    #                      profile=profile, feed=feed,
    #                     ).delete()