'''笔记本静态页面'''

import imp
from django.shortcuts import render,redirect
from django.http import *
from django.conf import settings
from django.db.models import Q

from Notebook.models import *
from Notebook.api.common import *

# 主页
def index(request):
    if not is_login(request): return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    notes_to_edit = note.objects.filter(isPending=True,directory__user=request.user)
    context = {
        'notes_to_edit':notes_to_edit
    }
    return render(request,'Notebook/index.html',context)

# 目录->所有目录
def all_directory(request):
    if not is_login(request): return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    dirs = directory.objects.filter(user=request.user)
    root_dir = dirs[0]
    context = {
        'root_dir':root_dir
    }
    return render(request,'Notebook/directory/allDirectories.html',context)

# 目录->目录内笔记列表详情
def directory_notelist(request,directory_id):
    if not is_login(request): return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    dir = directory.objects.get(id=directory_id)
    user = request.user
    if user != dir.user: return HttpResponseForbidden('您无权查看此目录')
    
    dirs = directory.objects.filter(user=request.user)
    root_dir = dirs[0]
    parents_directories = []
    children_directories = []

    #拉取所有父目录（crumb nav）
    directory_parent = None
    try: directory_parent = directory.objects.get(Q(first_child=dir)|Q(next_brother=dir))
    except: pass
    dir_temp = dir
    while(directory_parent):
        if dir_temp == directory_parent.first_child:
            parents_directories.append(directory_parent)
        dir_temp = directory_parent
        try:
            directory_parent = directory.objects.get(Q(first_child=dir_temp)|Q(next_brother=dir_temp))
        except Exception as e:
            break
    parents_directories.reverse()
    #拉取所有子目录（子目录列表）
    try:
        dir_temp = dir
        directory_child = dir_temp.first_child
        while(directory_child):
            children_directories.append(directory_child)
            directory_child = directory_child.next_brother
    except: pass
    notes_pintop = note.objects.filter(directory=dir,isPinTop=True).order_by('title')
    notes_not_pintop = note.objects.filter(directory=dir,isPinTop=False).order_by('title')
    

    context = {
        'directory' : dir,
        'directory_parents' : parents_directories,
        'directory_children' : children_directories,
        'notes_pintop' : notes_pintop,
        'notes_not_pintop' : notes_not_pintop,
        'root_dir': root_dir
    }
    return render(request,'Notebook/directory/notelist.html',context)

# 笔记详情
def note_detail(request,note_id):
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

# 笔记->编辑
def note_edit(request,note_id):
    if not is_login(request): return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    noteToEdit = note.objects.get(id=note_id)
    user = request.user
    if user != noteToEdit.user: return HttpResponseForbidden('您无权操作该笔记')
    
    context = {
        'note' : noteToEdit
    }
    return render(request,'Notebook/note/edit.html',context)

# 笔记->新增
def note_new(request,directory_id):
    if not is_login(request): return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    user = request.user
    dir = directory.objects.get(id=directory_id)
    if user != dir.user: return HttpResponseForbidden('您无权在此目录中新增笔记')
    
    context = {
        'directory':dir
    }
    return render(request,'Notebook/directory/newNote.html',context)
