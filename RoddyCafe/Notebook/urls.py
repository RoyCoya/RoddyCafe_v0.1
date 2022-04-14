from django.urls import path
from . import views

urlpatterns = [
	#静态页面url
	#目录相关
	path('', views.index, name='Notebook_index'),
	path('directory/', views.directory, name='Notebook_directory'),
	path('directory/<int:directory_id>/', views.directory_notelist, name='Notebook_directory_notelist'),
	#笔记相关
	path('note/<int:note_id>/', views.note, name='Notebook_note_detail'),
	path('note/<int:note_id>/edit/', views.note_edit, name='Notebook_note_edit'),


	#接口url
	path('directory/<int:directory_id>/delete/', views.api_directory_delete, name='api_Notebook_directory_delete'),
	path('note/<int:note_id>/delete/', views.api_note_delete, name='api_Notebook_note_delete'),
]