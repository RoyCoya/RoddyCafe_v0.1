from django.urls import path
from . import views

'''页面'''
pages = [
	path('', views.index, name='AFdian_index'),
]

'''接口'''
apis = [
	# path('new/', views.api_add_item, name='api_Ranking_add_item'),
]

urlpatterns = pages + apis