from django.urls import path
from . import views

urlpatterns = [
	path('', views.profile, name='AchievementNet_profile'),
]