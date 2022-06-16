from django.urls import path
from . import views

urlpatterns = [
	path('', views.homepage, name='LifeStream_homepage'),
]