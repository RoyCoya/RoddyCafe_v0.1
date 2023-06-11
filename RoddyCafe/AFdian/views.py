from django.conf import settings
from django.http import *
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from AFdian.page import index as page_index

def index(request): return page_index.index(request)