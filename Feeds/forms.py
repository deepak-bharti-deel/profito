from django import forms

from .models import Feed

class FeedForm(forms.ModelForm):
	class Meta:
		model = Feed
		fields = ('post','post_pic')
