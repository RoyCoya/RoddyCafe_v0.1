from django.urls import path
from . import views

'''页面'''
pages = [
	path('', views.index, name='MovieRank_index'),
]

'''接口'''
apis = [
	path('newmovie/', views.api_add_movie, name='api_MovieRank_add_movie'),
]

urlpatterns = pages + apis