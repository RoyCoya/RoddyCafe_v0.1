from django.conf import settings
from django.shortcuts import render,redirect
from django.http import *

from Notebook.models import *
from Notebook.api.common import *

# 笔记详情
def detail(request,note_id):
    if not is_login(request): return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    user = request.user
    noteToView = note.objects.get(id=note_id)
    if user != noteToView.user: return HttpResponseForbidden('您无权查看该笔记')

    dirs = directory.objects.filter(user=request.user)
    root_dir = dirs[0]
    
    context = {
        'note' : noteToView,
        'root_dir':root_dir,
    }
    return render(request,'Notebook/note/detail.html',context)

# 笔记编辑
def edit(request,note_id):
    if not is_login(request): return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    noteToEdit = note.objects.get(id=note_id)
    user = request.user
    if user != noteToEdit.user: return HttpResponseForbidden('您无权操作该笔记')
    
    context = {
        'note' : noteToEdit
    }
    return render(request,'Notebook/note/edit.html',context)

# 新增笔记
def new(request,directory_id):
    if not is_login(request): return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    user = request.user
    dir = directory.objects.get(id=directory_id)
    if user != dir.user: return HttpResponseForbidden('您无权在此目录中新增笔记')
    
    context = {
        'directory':dir
    }
    return render(request,'Notebook/directory/newNote.html',context)