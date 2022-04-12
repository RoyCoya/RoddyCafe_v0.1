from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .models import notebook_directory, notebook_note

# Create your views here.

###静态页面

#笔记库主页
def index(request):
    return render(request,'Notebook/index.html')

#目录
def directory(request):
    directories = notebook_directory.objects.all()
    context = {
        'Directories':directories
    }
    return render(request,'Notebook/directory/directory.html',context)

#指定目录的笔记列表
def notelist(request,directory_id):
    directory = notebook_directory.objects.get(directory_id=directory_id)
    notes = notebook_note.objects.filter(note_directory=directory)
    context = {
        'directory' : directory,
        'notes' : notes,
    }
    return render(request,'Notebook/directory/notelist.html',context)

###

###接口

###

###通用方法

###