from django.shortcuts import render
from django.http import HttpResponse

from CafeFrame.page import entrance as CafeEntrance

# 咖啡屋门口
def entrance(request): return CafeEntrance.doorway(request)