from django.shortcuts import render, redirect
from .models import *
from .forms import *

def index(request):
	posts = Content.objects.all().order_by("-date_posted")
	context = {
		'posts': posts
	}
	return render(request, "the_hub/index.html", context)


def hub_post(request):
	form = UploadHubPost()

	if request.method == "POST":
		form = UploadHubPost(request.POST)
		if form.is_valid():
			form.save()
			return redirect("hub_index")

	context = {
		'form': form
	}
	return render(request, "the_hub/hub_post.html", context)