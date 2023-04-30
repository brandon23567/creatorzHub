from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name="index"),
	path('auth_home/', views.auth_home, name="auth_home"),
	path('auth_home/community_detail/<int:pk>/', views.community_detail, name="community_detail"),
	path('signup/', views.signup, name="signup"),
	path('signin/', views.signin, name="signin"),
	path('auth_home/signout/', views.signout, name="signout"),
	path('auth_home/upload_post/', views.upload_post, name="upload_post"),
	path('auth_home/create_community/', views.create_community, name="create_community"),
]