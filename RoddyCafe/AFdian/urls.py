from django.urls import path
from . import views

'''页面'''
pages = [
	path('', views.index, name='AFdian_index'),
]

'''接口'''
apis = [
	path('save_token/', views.api_save_auth_token, name='api_AFdian_save_auth_token'),
]

urlpatterns = pages + apis