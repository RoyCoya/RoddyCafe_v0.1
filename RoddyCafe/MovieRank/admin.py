import imp
from django.contrib import admin
from .models import *

# Register your models here.
#笔记
class admin_movie(admin.ModelAdmin):
	list_display = [
		'id',
        'name',
        'poster',
        'pre',
        'next',
        'remarks',
]
admin.site.register(movie, admin_movie)