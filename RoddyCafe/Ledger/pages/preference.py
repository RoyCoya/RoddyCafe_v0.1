from django.conf import settings
from django.shortcuts import render,redirect

from CafeFrame.api.common import is_login

# 设置页面
def preference(request):
    if not is_login(request): return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    context = {}
    return render(request,'Ledger/preference/preference.html',context)