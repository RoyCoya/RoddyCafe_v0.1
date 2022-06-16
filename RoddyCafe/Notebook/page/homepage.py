from django.conf import settings
from django.shortcuts import render,redirect

from Notebook.models import *
from CafeFrame.api.common import is_login

# 主页
def homepage(request):
    if not is_login(request): return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    unfinished_notes = note.objects.filter(isPending=True,directory__user=request.user)
    dirs = directory.objects.filter(user=request.user)
    root_dir = dirs[0]

    # 按目录对笔记分组
    unfinished_notes_groupby_dirs = unfinished_notes.values('directory').distinct()
    for dir in unfinished_notes_groupby_dirs:
        dir['directory'] = directory.objects.get(id=dir['directory'])
        dir['notes'] = []
    for unfinished_note in unfinished_notes:
        for dir in unfinished_notes_groupby_dirs:
            if dir['directory'] == unfinished_note.directory:
                dir['notes'].append(unfinished_note)
    print(unfinished_notes_groupby_dirs)
    context = {
        'unfinished_notes_groupby_dirs' : unfinished_notes_groupby_dirs,
        'root_dir' : root_dir,
    }
    
    return render(request,'Notebook/homepage/homepage.html',context)