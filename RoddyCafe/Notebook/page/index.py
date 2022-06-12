from django.conf import settings
from django.shortcuts import render,redirect

from Notebook.models import *
from CafeFrame.api.common import is_login

# 主页
def homepage(request):
    if not is_login(request): return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    notes_to_edit = note.objects.filter(isPending=True,directory__user=request.user)
    context = {
        'notes_to_edit':notes_to_edit
    }
    return render(request,'Notebook/index/homepage.html',context)