from django.shortcuts import render
from django.http import HttpResponse

from CafeFrame.page import ground_floor
from CafeFrame.api import lobby as api_lobby

'''页面'''
# 咖啡屋大厅
def lobby(request): return ground_floor.lobby(request)

'''接口'''
def api_directory_new(request): return api_lobby.new_mastur(request)