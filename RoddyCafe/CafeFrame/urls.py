from django.urls import path
from . import views

pages = [
	path('', views.lobby, name='RoddyCafe_lobby'),
]

apis = [
	path('new_mastur/', views.api_directory_new, name='api_CafeFrame_new_mastur')
]

urlpatterns = pages + apis