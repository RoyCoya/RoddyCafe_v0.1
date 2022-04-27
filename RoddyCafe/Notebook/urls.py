from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
	#静态页面url
	#目录相关
	path('', views.index, name='Notebook_index'),
	path('directory/', views.directory, name='Notebook_directory'),
	path('directory/<int:directory_id>/', views.directory_notelist, name='Notebook_directory_notelist'),
	path('directory/<int:directory_id>/newnote/', views.note_new, name='Notebook_note_new'),
	#笔记相关
	path('note/<int:note_id>/', views.note, name='Notebook_note_detail'),
	path('note/<int:note_id>/edit/', views.note_edit, name='Notebook_note_edit'),
	


	#接口url
	path('directory/<int:directory_id>/newnote/save/', views.api_note_new_save, name='api_Notebook_directory_newNote'),
	path('directory/<int:directory_id>/delete/', views.api_directory_delete, name='api_Notebook_directory_delete'),
	path('directory/new/save', views.api_directory_new_save, name='api_Notebook_directory_new_save'),
	path('note/<int:note_id>/edit/save', views.api_note_save, name='api_Notebook_note_save'),
	path('note/<int:note_id>/delete/', views.api_note_delete, name='api_Notebook_note_delete'),
	path('note/uploadimg/', views.api_userfile_upload_img, name='api_Notebook_userfile_upload_img'),
	path('note/uploadvideo/', views.api_userfile_upload_video, name='api_Notebook_userfile_upload_video'),
]