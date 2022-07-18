from django.conf import settings
from django.shortcuts import render,redirect
from django.db.models import Q

from CafeFrame.api.common import is_login
from Notebook.models import note, directory
from Notebook.api.common import get_notification_count

# 待办主页面
def todo(request):
    if not is_login(request): return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    unfinished_notes = note.objects.filter(isUnfinished=True,directory__user=request.user).order_by('-editDate')

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
        except Exception as e: pass
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
    
    todo_count, share_count = get_notification_count(request.user)
    context = {
        'unfinished_notes_groupby_dir' : unfinished_notes_groupby_dir,
        'todo_count' : todo_count,
        'share_count' : share_count,
    }
    return render(request,'Notebook/todo/todo.html',context)