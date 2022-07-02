from django.shortcuts import render, redirect
from django.conf import settings

from CafeFrame.api.common import is_login

# 大厅
def lobby(request):
    return render(request,'CafeFrame/ground_floor/lobby.html')