from django.http import *
from django.urls import reverse
from django.shortcuts import redirect
from django.conf import settings

from CafeFrame.models import masturbation
from CafeFrame.api.common import is_login

def new_mastur(request):
    if not is_login(request): return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    if request.user.username != 'RockyRoo': return HttpResponseBadRequest('您无权操作此功能')
    masturbation.objects.create()
    return HttpResponseRedirect(reverse('RoddyCafe_lobby'))