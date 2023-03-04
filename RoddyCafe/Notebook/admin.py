from django.contrib import admin
from .models import *

#笔记目录
class admin_directory(admin.ModelAdmin):
	list_display = [
        'id',
        'user',
		'name',
        'discription',
        'first_child',
        'next_brother',
]
admin.site.register(directory,admin_directory)

#笔记
class admin_note(admin.ModelAdmin):
	list_display = [
		'id',
        'user',
        'title',
        'directory',
        'isPinTop',
        'isUnfinished',
        'createDate',
        'editDate',
]
admin.site.register(note,admin_note)

#笔记提醒
admin.site.register(alert)
#用户文件
class admin_note_file(admin.ModelAdmin):
	list_display = [
		'id',
        'note',
]
admin.site.register(note_file,admin_note_file)