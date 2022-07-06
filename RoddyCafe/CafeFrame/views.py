from django.shortcuts import render
from django.http import HttpResponse

from CafeFrame.page import ground_floor

# 咖啡屋大厅
def lobby(request): return ground_floor.lobby(request)