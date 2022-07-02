from django.conf import settings
from django.shortcuts import render,redirect

from Notebook.models import directory
from CafeFrame.api.common import is_login
from Notebook.api.common import get_notification_count

# 主页
def homepage(request):
    if not is_login(request): return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    dirs = directory.objects.filter(user=request.user)
    root_dir = dirs[0]

    todo_count, share_count = get_notification_count(request.user)
    context = {
        'root_dir' : root_dir,
        'todo_count' : todo_count,
        'share_count' : share_count,
    }
    return render(request,'Notebook/homepage/homepage.html',context)