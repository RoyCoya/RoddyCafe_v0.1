from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
from django.http import *
from django.urls import reverse

from CafeFrame.api.common import is_login
from .models import movie

def get_movie_list():
    movie_list = []
    pointer = movie.objects.get(pre=None)
    while pointer.next:
        movie_list.append(pointer)
        pointer = pointer.next
    movie_list.append(pointer)
    return movie_list

def index(request):
    if not is_login(request): return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    user = request.user
    if user.id >3 : return HttpResponseForbidden('您无权查看该页面')

    movies = get_movie_list()
    
    context = {
        'movies' : movies
    }
    return render(request,'MovieRank/index.html',context)

def api_add_movie(request):
    if not is_login(request): return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    user = request.user
    if user.id >3 : return HttpResponseForbidden('您无权操作')

    movies = get_movie_list()
    new_rank = int(request.POST['rank']) - 1
    pre = next = None
    if new_rank <= 0 : next = movies[0]
    elif new_rank <= len(movies) - 1 : pre, next = movies[new_rank - 1], movies[new_rank]
    else : pre = movies[-1]
    new_movie = movie.objects.create(
        name = request.POST['name'],
        remarks = request.POST['remarks'],
    )
    new_movie.pre, new_movie.next = pre, next
    new_movie.save()
    if pre:
        pre.next = new_movie
        pre.save()
    if next:
        next.pre = new_movie
        next.save()

    try:
        new_movie.poster = request.FILES['poster']
        new_movie.save()
    except Exception as e: print(e)

    return HttpResponseRedirect(reverse('MovieRank_index',args=()))