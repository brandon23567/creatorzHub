from django import forms
from django.forms import ModelForm
from .models import *

class CreateCommunityForm(forms.ModelForm):
	community_name = forms.CharField(widget=forms.TextInput(attrs={"class": "community_name_input", "placeholder": "Please a name for your community"}))
	community_description = forms.CharField(widget=forms.Textarea(attrs={"class": "description_input", "placeholder": "Please enter what your community is all about"}))
	class Meta:
		model = Community
		fields = ("community_name", "community_description", "community_image")

class CreatePostForm(forms.ModelForm):
	username = forms.CharField(widget=forms.TextInput(attrs={"class": "username_input", "placeholder": "Please a name for your community"}))
	body = forms.CharField(widget=forms.Textarea(attrs={"class": "body_input", "placeholder": "Please enter what you want to say here"}))
	class Meta:
		model = CommunityPost
		fields = ("community", "username", "body")