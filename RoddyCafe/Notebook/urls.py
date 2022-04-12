from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='Notebook_index'),
	path('directory/', views.directory, name='Notebook_directory'),
	path('directory/<int:directory_id>', views.notelist, name='Notebook_directory_notelist'),
]