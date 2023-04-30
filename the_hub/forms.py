from django import forms
from django.forms import ModelForm
from .models import *

class UploadHubPost(forms.ModelForm):
	title = forms.CharField(widget=forms.TextInput(attrs={"class": "title_input", "placeholder": "Please enter a title for your video"}))
	short_description = forms.CharField(widget=forms.Textarea(attrs={"class": "description_input", "placeholder": "Please enter a short description of your video"}))
	video_link = forms.CharField(widget=forms.TextInput(attrs={"class": "video_link_input", "placeholder": "Please enter your video link"}))
	class Meta:
		model = Content
		fields = ("title", "short_description", "video_link")