from django.shortcuts import render, redirect
from django.conf import settings

from CafeFrame.api.common import is_login

def homepage(request):
    if not is_login(request): return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    return render(request, 'LifeStream/homepage/homepage.html')