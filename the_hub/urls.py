from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name="hub_index"),
	path('hub_post/', views.hub_post, name="hub_post")
]