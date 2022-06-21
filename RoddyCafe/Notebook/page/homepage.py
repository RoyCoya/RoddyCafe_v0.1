from django.conf import settings
from django.shortcuts import render,redirect
from django.db.models import Q

from Notebook.models import *
from CafeFrame.api.common import is_login

# 主页
def homepage(request):
    if not is_login(request): return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    unfinished_notes = note.objects.filter(isPending=True,directory__user=request.user).order_by('-editDate')
    dirs = directory.objects.filter(user=request.user)
    root_dir = dirs[0]
    
    # 按目录对笔记分组
    dir_ids = []
    unfinished_notes_groupby_dir = []
    for unfinished_note in unfinished_notes:
        dir_id = unfinished_note.directory.id
        if dir_id in dir_ids:
            continue
        else:
            dir_ids.append(dir_id)
    for dir_id in dir_ids:
        group = {}
        dir = directory.objects.get(id=dir_id)
        group['directory'] = dir
        parents_directories = []
        directory_parent = None
        try: directory_parent = directory.objects.get(Q(first_child=dir)|Q(next_brother=dir))
        except Exception as e: print(e)
        dir_temp = dir
        while(directory_parent):
            if dir_temp == directory_parent.first_child:
                parents_directories.append(directory_parent)
            dir_temp = directory_parent
            try:
                directory_parent = directory.objects.get(Q(first_child=dir_temp)|Q(next_brother=dir_temp))
            except Exception as e: directory_parent=None
        parents_directories.reverse()
        
        group['parents'] = parents_directories
        group['notes'] = []
        unfinished_notes_groupby_dir.append(group)
    # 组装成dict
    for unfinished_note in unfinished_notes:
        for dir in unfinished_notes_groupby_dir:
            if dir['directory'] == unfinished_note.directory:
                dir['notes'].append(unfinished_note)

    context = {
        'unfinished_notes_groupby_dir' : unfinished_notes_groupby_dir,
        'root_dir' : root_dir,
    }
    
    return render(request,'Notebook/homepage/homepage.html',context)