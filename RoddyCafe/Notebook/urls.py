from unicodedata import name
from django.urls import path
from . import views

'''页面'''
pages = [
	# 四个主页面：主页、待办、共享、设置
	path('', views.homepage, name='Notebook_homepage'),
	path('todo/', views.todo, name='Notebook_todo'),
	path('share/', views.share, name='Notebook_share'),
	path('configurations/', views.configurations, name='Notebook_configurations'),
	# 目录和笔记
	path('directory/<int:directory_id>/is_from_homepage/<int:is_from_homepage>/', views.directory_specific, name='Notebook_directory_specific'),
	path('note/<int:note_id>/', views.note_detail, name='Notebook_note_detail'),
	path('note/new/<int:directory_id>/', views.note_new, name='Notebook_note_new'),
	path('note/<int:note_id>/edit/is_from_homepage/<int:is_from_homepage>/', views.note_edit, name='Notebook_note_edit'),
]

'''接口'''
apis = [
	# 目录
	path('directory/new/<int:directory_id>/', views.api_directory_new, name='api_Notebook_directory_new'),
	path('directory/<int:directory_id>/delete/', views.api_directory_delete, name='api_Notebook_directory_delete'),
	path('directory/<int:directory_id>/changename/', views.api_directory_edit_name, name='api_Notebook_directory_edit_name'),
	path('directory/<int:directory_id>/changediscription/', views.api_directory_edit_discription, name='api_Notebook_directory_edit_discription'),
	path('directory/<int:dir_to_move_id>/move/parent/<int:parent_id>/child/<int:child_id>/childtype/<int:is_first_child>/', views.api_directory_move, name='api_Notebook_directory_move'),

	# 笔记
	path('note/<int:note_id>/edit/save/', views.api_note_edit, name='api_Notebook_note_save'),
	path('note/<int:note_id>/delete/', views.api_note_delete, name='api_Notebook_note_delete'),
	path('note/<int:note_id>/moveto/directory/<int:directory_id>/', views.api_note_move, name='api_Notebook_note_move'),
	path('note/<int:note_id>/setpintop/', views.api_note_switch_pintop, name='api_Notebook_note_switch_pintop'),
	path('note/<int:note_id>/setpending/', views.api_note_switch_pending, name='api_Notebook_note_switch_pending'),
	path('note/<int:note_id>/uploadimg/', views.api_wangeditor_upload_img, name='api_Notebook_note_upload_img'),
	path('note/<int:note_id>/uploadvideo/', views.api_wangeditor_upload_video, name='api_Notebook_note_upload_video'),
]

urlpatterns = pages + apis