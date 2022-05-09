from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
	#静态页面url
	#用户相关
	#目录相关
	path('', views.index, name='Notebook_index'),
	path('directory/', views.all_directory, name='Notebook_directory'),
	path('directory/<int:directory_id>/', views.directory_notelist, name='Notebook_directory_notelist'),
	path('directory/<int:directory_id>/newnote/', views.note_new, name='Notebook_note_new'),
	#笔记相关
	path('note/<int:note_id>/', views.note_detail, name='Notebook_note_detail'),
	path('note/<int:note_id>/edit/', views.note_edit, name='Notebook_note_edit'),

	#接口url
	#目录相关
	path('directory/<int:directory_id>/newnote/save/', views.api_note_new_save, name='api_Notebook_directory_newNote'),
	path('directory/<int:directory_id>/delete/', views.api_directory_delete, name='api_Notebook_directory_delete'),
	path('directory/new/save/<int:directory_id>', views.api_directory_new_save, name='api_Notebook_directory_new_save'),
	path('directory/<int:dir_to_move_id>/move/parent/<int:parent_id>/child/<int:child_id>/childtype/<int:is_first_child>', views.api_directory_change_position, name='api_Notebook_move_directory'),
	#笔记相关
	path('note/<int:note_id>/edit/save', views.api_note_save, name='api_Notebook_note_save'),
	path('note/<int:note_id>/delete/', views.api_note_delete, name='api_Notebook_note_delete'),
	path('note/<int:note_id>/changedir/<int:directory_id>/', views.api_note_change_directory, name='api_Notebook_note_change_directory'),
	path('note/<int:note_id>/setpintop/', views.api_note_switch_pintop, name='api_Notebook_note_switch_pintop'),
	path('note/<int:note_id>/setpending/', views.api_note_switch_pending, name='api_Notebook_note_switch_pending'),
	path('note/uploadimg/', views.api_userfile_upload_img, name='api_Notebook_userfile_upload_img'),
	path('note/uploadvideo/', views.api_userfile_upload_video, name='api_Notebook_userfile_upload_video'),
]