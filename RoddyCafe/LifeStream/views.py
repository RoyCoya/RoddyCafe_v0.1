from django.shortcuts import render
from django.http import HttpResponse

from LifeStream.page import index

def homepage(request): return index.homepage(request)