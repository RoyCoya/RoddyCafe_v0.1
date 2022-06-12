from django.conf import settings
from django.shortcuts import render,redirect
from django.http import *
from django.db.models import Q

from Notebook.models import *
from CafeFrame.api.common import is_login

# 所有目录
def all(request):
    if not is_login(request): return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    dirs = directory.objects.filter(user=request.user)
    root_dir = dirs[0]
    context = {
        'root_dir':root_dir
    }
    return render(request,'Notebook/directory/allDirectories.html',context)

# 目录内笔记列表详情
def notelist(request,directory_id):
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