from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='Notebook_index'),
]