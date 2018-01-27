from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models 
from django.utils.encoding import python_2_unicode_compatible 
from django.utils.html import escape
from django.utils.translation import ugettext_lazy as _

import bleach 
from Users.models import Profile

     
@python_2_unicode_compatible     
class Feed(models.Model):  
    user = models.ForeignKey(User, related_name="from_user", null=True, on_delete='models.cascade') 

    date = models.DateTimeField(auto_now_add=True)
    post = models.TextField(max_length=255)
    post_pic = models.ImageField(null=True, blank=True, 
            height_field="height_field",
            width_field="width_field")    
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)     
    ad_value    = models.IntegerField(default=0)

    class Meta:
        verbose_name = _('Feed')
        verbose_name_plural = _('Feeds')
        ordering = ('-date',)

    def __str__(self):
        return self.post 


    def linkfy_post(self):
        return bleach.linkify(escape(self.post))  

    # def get_absolute_url(self):
    #     return reverse('detail', kwargs={'slug': self.slug})
    def post_pic_url(self):
        return "http://127.0.0.1:8000"+self.post_pic.url