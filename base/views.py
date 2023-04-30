from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import *
from .forms import *

def index(request):

	posts = CommunityPost.objects.all().order_by("-date_posted")
	communitys = Community.objects.all().order_by("-date_created")

	context = {
		'posts': posts,
		'communitys': communitys,
	}

	return render(request, "base/index.html", context)

def auth_home(request):

	posts = CommunityPost.objects.all().order_by("-date_posted")
	communitys = Community.objects.all().order_by("-date_created")

	context = {
		'posts': posts,
		'communitys': communitys,
	}
	return render(request, "base/auth_home.html", context)

def community_detail(request, pk):
	community = get_object_or_404(Community, id=pk)
	context = {
		'community': community
	}
	return render(request, "base/community_detail.html", context)

def upload_post(request):
	form = CreatePostForm()

	if request.method == "POST":
		form = CreatePostForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("auth_home")

	context = {
		'form': form
	}
	return render(request, "base/upload_post.html", context)

def create_community(request):

	form = CreateCommunityForm()

	if request.method == "POST":
		form = CreateCommunityForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("auth_home")

	context = {
		'form': form
	}
	return render(request, "base/create_community.html", context)

def signup(request):

	if request.method == "POST":
		username = request.POST["username"]
		email = request.POST["email"]
		password = request.POST["password"]
		confirm_password = request.POST["confirm_password"]

		if password == confirm_password:
			if User.objects.filter(username=username).exists():
				messages.info(request, 'Email or username already taken')

			else:
				user = User.objects.create_user(username=username, email=email, password=password)
				user.set_password(password)
				user.save()
				return redirect("signin")
	return render(request, "base/signup.html")

def signin(request):

	if request.method == "POST":
		username = request.POST["username"]
		password = request.POST["password"]

		user = auth.authenticate(username=username, password=password)

		if user is not None:
			auth.login(request, user)
			return redirect('auth_home')
		else:
			messages.info(request, "Invalid username or password")
			return redirect("signin")
	return render(request, "base/signin.html")

def signout(request):
	auth.logout(request)
	return redirect("index")