from unicodedata import name
from django.urls import path
from . import views

'''页面'''
pages = [
	# 目录
	path('', views.index_homepage, name='Notebook_homepage'),
	path('directory/', views.all_directory, name='Notebook_directory'),
	path('directory/<int:directory_id>/', views.directory_notelist, name='Notebook_directory_notelist'),
	# 笔记
	path('directory/<int:directory_id>/newnote/', views.note_new, name='Notebook_note_new'),
	path('note/<int:note_id>/', views.note_detail, name='Notebook_note_detail'),
	path('note/<int:note_id>/edit/', views.note_edit, name='Notebook_note_edit'),
]

'''接口'''
apis = [
	# 目录
	path('directory/new/<int:directory_id>/', views.api_directory_new, name='api_Notebook_directory_new'),
	path('directory/<int:directory_id>/delete/', views.api_directory_delete, name='api_Notebook_directory_delete'),
	path('directory/<int:directory_id>/changediscription/', views.api_directory_edit_discription, name='api_Notebook_directory_edit_discription'),
	path('directory/<int:dir_to_move_id>/move/parent/<int:parent_id>/child/<int:child_id>/childtype/<int:is_first_child>/', views.api_directory_move, name='api_Notebook_directory_move'),

	# 笔记
	path('directory/<int:directory_id>/newnote/save/', views.api_note_new, name='api_Notebook_note_new'),
	path('note/<int:note_id>/edit/save/', views.api_note_edit, name='api_Notebook_note_save'),
	path('note/<int:note_id>/delete/', views.api_note_delete, name='api_Notebook_note_delete'),
	path('note/<int:note_id>/moveto/directory/<int:directory_id>/', views.api_note_move, name='api_Notebook_note_move'),
	path('note/<int:note_id>/setpintop/', views.api_note_switch_pintop, name='api_Notebook_note_switch_pintop'),
	path('note/<int:note_id>/setpending/', views.api_note_switch_pending, name='api_Notebook_note_switch_pending'),

	# wangeditor
	path('note/uploadimg/', views.api_wangeditor_upload_img, name='api_Notebook_wangeditor_upload_img'),
	path('note/uploadvideo/', views.api_wangeditor_upload_video, name='api_Notebook_wangeditor_upload_video'),
]

urlpatterns = pages + apis