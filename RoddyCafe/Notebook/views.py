import imp
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import notebook_directory, notebook_note
from django.urls import reverse

# Create your views here.

###静态页面

#主页
def index(request):
    return render(request,'Notebook/index.html')

#目录->所有目录
def directory(request):
    directories = notebook_directory.objects.all()
    context = {
        'Directories':directories
    }
    return render(request,'Notebook/directory/allDirectories.html',context)

#目录->目录内笔记列表详情
def directory_notelist(request,directory_id):
    directory = notebook_directory.objects.get(directory_id=directory_id)
    notes = notebook_note.objects.filter(note_directory=directory)
    context = {
        'directory' : directory,
        'notes' : notes,
    }
    return render(request,'Notebook/directory/notelist.html',context)

#笔记
def note(request,note_id):
    note = notebook_note.objects.get(note_id=note_id)
    context = {
        'note' : note
    }
    return render(request,'Notebook/note/detail.html',context)

#笔记->编辑
def note_edit(request,note_id):
    note = notebook_note.objects.get(note_id=note_id)
    context = {
        'note' : note
    }
    return render(request,'Notebook/note/edit.html',context)

###

###接口

#删除目录
#TODO：具体实现
def api_directory_delete(request,directory_id):
    directory = notebook_directory.objects.get(directory_id=directory_id)
    directory.delete()
    return HttpResponse('delete directory success')

#删除笔记
#TODO：补充判断
def api_note_delete(request,note_id):
    note = notebook_note.objects.get(note_id=note_id)
    directory = note.note_directory
    note.delete()
    return HttpResponseRedirect(reverse('Notebook_directory_notelist',args=(directory.directory_id,)))

###

###通用方法

###