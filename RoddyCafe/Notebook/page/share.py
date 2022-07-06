from django.conf import settings
from django.shortcuts import render,redirect

from CafeFrame.api.common import is_login
from Notebook.api.common import get_notification_count

# 待办主页面
def share(request):
    if not is_login(request): return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    
    todo_count, share_count = get_notification_count(request.user)
    context = {
        'todo_count' : todo_count,
        'share_count' : share_count,
    }
    return render(request,'Notebook/share/share.html',context)