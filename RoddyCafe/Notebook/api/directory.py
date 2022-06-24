'''目录操作'''
from django.db.models import Q
from django.conf import settings
from django.shortcuts import redirect
from django.http import *
from django.urls import reverse

from CafeFrame.api.common import is_login
from Notebook.models import *
from Notebook.api.common import func_getDirsToDelete_list

# 新增目录
def new(request, directory_id):
    if not is_login(request): return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

    new_directory = directory(
        user = request.user,
        name = request.POST['directory_name'],
        discription = request.POST['directory_discription']
    )
    new_directory.save()

    # position格式：action_parentID_childID
    postion = str(request.POST['directory_position']).split('_')
    if len(postion)>1:
        parent = directory.objects.get(id=postion[1])
        child = None
        if postion[2]:
            child = directory.objects.get(id=postion[2])
        if child:
            isFirstChild = True if parent.first_child == child else False
            if isFirstChild:
                inserted_newDir = directory.objects.get(id=new_directory.id)
                parent.first_child = inserted_newDir
                parent.save()
                inserted_newDir.next_brother = child
                inserted_newDir.save()
            else:
                inserted_newDir = directory.objects.get(id=new_directory.id)
                parent.next_brother = inserted_newDir
                parent.save()
                inserted_newDir.next_brother = child
                inserted_newDir.save()
        else:
            isFirstChild = True if postion[3] == 'left' else False
            if isFirstChild:
                inserted_newDir = directory.objects.get(id=new_directory.id)
                parent.first_child = inserted_newDir
                parent.save()
            else:
                inserted_newDir = directory.objects.get(id=new_directory.id)
                parent.next_brother = inserted_newDir
                parent.save()
    else:
        dirs = directory.objects.filter(user=request.user)
        inserted_newDir = directory.objects.get(id=new_directory.id)
        root_dir = dirs[0]
        root_dir.first_child = inserted_newDir
        root_dir.save()
    
    return HttpResponseRedirect(reverse('Notebook_directory_specific',args=(new_directory.id, 0)))

# 删除目录
# TODO:删除后跳转至父目录（非数据结构的父节点）
def delete(request,directory_id):
    if not is_login(request): return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    dir = directory.objects.get(id=directory_id)
    user = request.user
    if user != dir.user: return HttpResponseForbidden('您无权删除此目录')
    # user_root_dir = directory.objects.filter(user=user)[0]

    parent = directory.objects.get(Q(first_child=dir)|Q(next_brother=dir))
    isFirstChild = False if parent.first_child != dir else True
    if isFirstChild:
        parent.first_child = dir.next_brother
        parent.save()
        delete_list = [dir]
        if dir.first_child:
            delete_list = func_getDirsToDelete_list(dir.first_child,delete_list)
        for dir in delete_list: dir.delete()
    else:
        parent.next_brother = dir.next_brother
        parent.save()
        delete_list = [dir]
        if dir.first_child:
            delete_list = func_getDirsToDelete_list(dir.first_child,delete_list)
        for dir in delete_list: dir.delete()      
    
    # if parent == user_root_dir: return HttpResponseRedirect(reverse('Notebook_directory_all'))
    # else: return HttpResponseRedirect(reverse('Notebook_directory_specific',args=(parent.id,)))
    return HttpResponseRedirect(reverse('Notebook_directory_all'))

# 目录移动位置
def move(request,dir_to_move_id,parent_id,child_id,is_first_child):
    if not is_login(request): return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    dir_to_move = directory.objects.get(id=dir_to_move_id)
    user = request.user
    if user != dir_to_move.user: return HttpResponseForbidden('您无权移动此目录')
    
    #抽离需要移动的目录，脱开的两端进行连接
    parent = directory.objects.get(Q(first_child=dir_to_move)|Q(next_brother=dir_to_move))
    is_dir_to_move_first_child = False if parent.first_child != dir_to_move else True
    print(parent.first_child)
    if is_dir_to_move_first_child:
        parent.first_child = dir_to_move.next_brother
    else:
        parent.next_brother = dir_to_move.next_brother
    parent.save()
    dir_to_move.next_brother = None
    dir_to_move.save()
    print(parent.first_child)

    #插入新位置
    target_parent = directory.objects.get(id=parent_id)
    target_child = None
    if child_id:
        target_child = directory.objects.get(id=child_id)
    print(target_parent.first_child)
    if target_child:
        is_target_child_first_child = False if target_parent.first_child != target_child else True
        if is_target_child_first_child:
            target_parent.first_child = dir_to_move
        else:
            target_parent.next_brother = dir_to_move
        dir_to_move.next_brother = target_child
    else:
        if is_first_child:
            target_parent.first_child = dir_to_move
        else:
            target_parent.next_brother = dir_to_move
    target_parent.save()
    dir_to_move.save()
    print(target_parent.first_child)

    return HttpResponseRedirect(reverse('Notebook_directory_specific',args=(dir_to_move_id, 0)))

# 目录更改名称
def edit_name(request,directory_id):
    if not is_login(request): return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    user = request.user
    dir = directory.objects.get(id=directory_id)
    if user != dir.user: return HttpResponseForbidden('您无权修改此目录的名称')

    dir.name = request.POST['directory_name']
    dir.save()

    return HttpResponseRedirect(reverse('Notebook_directory_specific',args=(directory_id, 0)))

# 目录更改描述
def edit_discription(request,directory_id):
    if not is_login(request): return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    user = request.user
    dir = directory.objects.get(id=directory_id)
    if user != dir.user: return HttpResponseForbidden('您无权修改此目录的描述')
    
    dir.discription = request.POST['directory_discription']
    dir.save()
    
    return HttpResponseRedirect(reverse('Notebook_directory_specific',args=(directory_id, 0)))