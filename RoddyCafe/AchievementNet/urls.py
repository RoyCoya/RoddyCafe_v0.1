from django.urls import path
from . import views

urlpatterns = [
	path('', views.homepage, name='AchievementNet_homepage'),
]