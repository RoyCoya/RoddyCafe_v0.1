from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
from django.http import *
from django.urls import reverse

from CafeFrame.api.common import is_login
from .models import RankItem

def get_item_list(type):
    item_list = []
    pointer = None
    try: pointer = RankItem.objects.get(pre=None, type=type)
    except: return item_list
    while pointer.next:
        item_list.append(pointer)
        pointer = pointer.next
    item_list.append(pointer)
    return item_list

def index(request):
    if not is_login(request): return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    user = request.user
    if user.id >3 : return HttpResponseForbidden('您无权查看该页面')

    type = 'movie'
    try: type = request.GET['type']
    except: pass
    type_in_Chinese = {
	    'movie': lambda: '电影',
		'anime': lambda: '番剧',
		'book': lambda: '图书',	
	}[type]
    rank_items = get_item_list(type)
    
    context = {
        'type_in_Chinese' : type_in_Chinese,
        'type' : type,
        'rank_items' : rank_items
    }
    return render(request,'Ranking/index.html',context)

def api_add_item(request):
    if not is_login(request): return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    user = request.user
    if user.id >3 : return HttpResponseForbidden('您无权操作')

    rank = request.POST['rank']
    name = request.POST['name']
    remarks = request.POST['remarks']
    type = request.POST['type']

    new_rank = int(rank) - 1
    rank_items = get_item_list(type)

    pre = next = None
    if len(rank_items) == 0 : 
        new_rank_item = RankItem.objects.create(
            name = name,
            remarks = remarks,
            type = type
        )
        try:
            new_rank_item.poster = request.FILES['poster']
            new_rank_item.save()
        except Exception as e: pass#print(e)
        return HttpResponseRedirect(reverse('Ranking_index', args=()) + '?type=' + type)
    if new_rank <= 0 : next = rank_items[0]
    elif new_rank <= len(rank_items) - 1 : pre, next = rank_items[new_rank - 1], rank_items[new_rank]
    else : pre = rank_items[-1]
    new_rank_item = RankItem.objects.create(
        name = name,
        remarks = remarks,
        type = type,
    )
    new_rank_item.pre, new_rank_item.next = pre, next
    new_rank_item.save()
    if pre:
        pre.next = new_rank_item
        pre.save()
    if next:
        next.pre = new_rank_item
        next.save()
    try:
        new_rank_item.poster = request.FILES['poster']
        new_rank_item.save()
    except Exception as e: pass#print(e)

    return HttpResponseRedirect(reverse('Ranking_index', args=()) + '?type=' + type)