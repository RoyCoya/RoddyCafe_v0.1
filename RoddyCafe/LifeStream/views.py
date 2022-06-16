from django.shortcuts import render
from django.http import HttpResponse

from LifeStream.page import homepage as page_homepage

def homepage(request): return page_homepage.homepage(request)