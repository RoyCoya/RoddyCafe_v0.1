from django.conf import settings
from django.shortcuts import render,redirect

from CafeFrame.api.common import is_login

# 历史记录
def history(request):
    if not is_login(request): return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    context = {}
    return render(request,'Ledger/history/history.html',context)