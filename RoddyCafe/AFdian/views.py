from django.conf import settings
from django.http import *
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from AFdian.page import index as page_index
from AFdian.api import AFdian as api_AFdian

def index(request): return page_index.index(request)
def api_save_auth_token(request): return api_AFdian.save_auth_token(request)