from django.contrib import admin
from .models import notebook_directory, notebook_note, notebook_note_alert
# Register your models here.

#笔记目录
class admin_notebook_directory(admin.ModelAdmin):
	list_display = [
		'directory_name',
        'directory_parentDir',
        'directory_discription',
        'directory_createdDate'
]
admin.site.register(notebook_directory,admin_notebook_directory)

#笔记
class admin_notebook_note(admin.ModelAdmin):
	list_display = [
		'note_id',
        'note_directory',
        'note_title',
        'note_pinTop',
        'note_pending',
        'note_createDate',
        'note_editDate'
]
admin.site.register(notebook_note,admin_notebook_note)

#笔记提醒
admin.site.register(notebook_note_alert)
