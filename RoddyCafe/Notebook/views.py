from django.conf import settings
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseForbidden,HttpResponseRedirect
from .models import directory, note, userfile
from django.urls import reverse
from django.core.files import File
from django.db.models import Q
from django.contrib.auth import logout

# Create your views here.

'''
静态页面
'''

#主页
def index(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
        return render(request,'Notebook/index.html')

#目录->所有目录
def all_directory(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
        dirs = directory.objects.filter(user=request.user)
        root_dir = dirs[0]
        context = {
            'root_dir':root_dir
        }
        return render(request,'Notebook/directory/allDirectories.html',context)

#目录->目录内笔记列表详情
def directory_notelist(request,directory_id):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
        dir = directory.objects.get(id=directory_id)
        if request.user != dir.user:
            return HttpResponseForbidden('您无权查看此页面')
        dir_temp = dir
        #拉取所有父目录
        directory_parent = False
        try:
            directory_parent = directory.objects.get(Q(first_child=dir)|Q(next_brother=dir))
        except Exception as e:
            pass
        parents_directories = []
        while(directory_parent):
            if dir_temp == directory_parent.first_child:
                parents_directories.append(directory_parent)
            dir_temp = directory_parent
            try:
                directory_parent = directory.objects.get(Q(first_child=dir_temp)|Q(next_brother=dir_temp))
            except Exception as e:
                break
        parents_directories.reverse()
        #拉取所有子目录
        children_directories = []
        try:
            dir_temp = dir
            directory_child = dir_temp.first_child
            while(directory_child):
                children_directories.append(directory_child)
                directory_child = directory_child.next_brother
        except Exception as e:
            pass
        notes_pintop = note.objects.filter(directory=dir,isPinTop=True).order_by('title')
        notes_not_pintop = note.objects.filter(directory=dir,isPinTop=False).order_by('title')
        dirs = directory.objects.filter(user=request.user)
        root_dir = dirs[0]
        context = {
            'directory' : dir,
            'directory_parents' : parents_directories,
            'directory_children' : children_directories,
            'notes_pintop' : notes_pintop,
            'notes_not_pintop' : notes_not_pintop,
            'root_dir': root_dir
        }
        return render(request,'Notebook/directory/notelist.html',context)

#笔记详情
def note_detail(request,note_id):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
        noteToView = note.objects.get(id=note_id)
        if request.user != noteToView.user:
            return HttpResponseForbidden('您无权查看此页面')
        dirs = directory.objects.filter(user=request.user)
        root_dir = dirs[0]
        context = {
            'note' : noteToView,
            'root_dir':root_dir,
        }
        return render(request,'Notebook/note/detail.html',context)

#笔记->编辑
def note_edit(request,note_id):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
        noteToEdit = note.objects.get(id=note_id)
        if request.user != noteToEdit.user:
            return HttpResponseForbidden('您无权查看此页面')
        context = {
            'note' : noteToEdit
        }
        return render(request,'Notebook/note/edit.html',context)

#笔记->新增
def note_new(request,directory_id):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
        dir = directory.objects.get(id=directory_id)
        if request.user != dir.user:
            return HttpResponseForbidden('您无权查看此页面')
        context = {
            'directory':dir
        }
        return render(request,'Notebook/directory/newNote.html',context)

'''
接口
'''

#删除目录
def api_directory_delete(request,directory_id):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
        dir = directory.objects.get(id=directory_id)
        if request.user != dir.user:
            return HttpResponseForbidden('您无权查看此页面')
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
        return HttpResponseRedirect(reverse('Notebook_directory'))

#根目录页面中新增目录
def api_directory_new_save(request, directory_id):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
        new_directory = directory(
            user = request.user,
            name = request.POST['directory_name'],
            discription = request.POST['directory_discription']
        )
        new_directory.save()
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
        if directory_id:
            dir = directory.objects.get(id=directory_id)
            return HttpResponseRedirect(reverse('Notebook_directory_notelist',args=(dir.id,)))
        else:
            return HttpResponseRedirect(reverse('Notebook_directory'))

#目录移动位置
def api_directory_change_position(request,dir_to_move_id,parent_id,child_id,is_first_child):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
        target_parent = directory.objects.get(id=parent_id)
        target_child = None
        if child_id:
            target_child = directory.objects.get(id=child_id)
        #分离需要移动的目录，两端连接
        dir_to_move = directory.objects.get(id=dir_to_move_id)
        parent = directory.objects.get(Q(first_child=dir_to_move)|Q(next_brother=dir_to_move))

        is_dir_to_move_first_child = False if parent.first_child != dir_to_move else True
        if is_dir_to_move_first_child:
            parent.first_child = dir_to_move.next_brother
        else:
            parent.next_brother = dir_to_move.next_brother
        print
        parent.save()
        dir_to_move.next_brother = None
        dir_to_move.save()
        #插入新位置
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
        return HttpResponse('directory moved success')

#新增笔记
def api_note_new_save(request,directory_id):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
        dir = directory.objects.get(id=directory_id)
        if request.user != dir.user:
            return HttpResponseForbidden('您无权查看此页面')
        new_note = note(
            directory=dir,
            user=request.user,
            title=request.POST['note_title'],
            content=request.POST['note_content'],
        )
        new_note.save()
        return HttpResponse(new_note.id)

#删除笔记
def api_note_delete(request,note_id):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
        noteDeleted = note.objects.get(id=note_id)
        if request.user != noteDeleted.user:
            return HttpResponseForbidden('您无权查看此页面')
        dir = noteDeleted.directory
        noteDeleted.delete()
        return HttpResponseRedirect(reverse('Notebook_directory_notelist',args=(dir.id,)))

#保存笔记编辑
def api_note_save(request,note_id):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
        noteEdited = note.objects.get(id=note_id)
        if request.user != noteEdited.user:
            return HttpResponseForbidden('您无权查看此页面')
        noteEdited.content = request.POST['note_content_edited']
        noteEdited.save()
        return HttpResponse('note saved successfully.')

#笔记更换目录
def api_note_change_directory(request,note_id,directory_id):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
        note_to_change_dir = note.objects.get(id=note_id)
        target_directory = directory.objects.get(id=directory_id)
        note_to_change_dir.directory = target_directory
        note_to_change_dir.save()
        return HttpResponseRedirect(reverse('Notebook_directory_notelist',args=(directory_id,)))

#笔记切换置顶状态
def api_note_switch_pintop(request,note_id):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
        note_to_set_pin = note.objects.get(id=note_id)
        note_to_set_pin.isPinTop = request.POST['pintop_checked'].title()
        note_to_set_pin.save()
        return HttpResponse("success to change note's pin status")

#笔记切换待编辑状态
def api_note_switch_pending(request,note_id):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
        note_to_set_pending = note.objects.get(id=note_id)
        note_to_set_pending.isPending = request.POST['pending_checked'].title()
        note_to_set_pending.save()
        return HttpResponse("success to change note's pending status")

#wangeditor上传图片
def api_userfile_upload_img(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
        fileUploaded = File(request.FILES.get('img_uploaded'))
        userfileUploaded = userfile(
            content=fileUploaded,
            user=request.user
        )
        userfileUploaded.save()
        return HttpResponse(
            '{"errno": 0,"data": {"url": "'+ userfileUploaded.content.url +'","href": "'+ userfileUploaded.content.url +'"}}',
            content_type='application/json'
        )

#wangeditor上传视频
def api_userfile_upload_video(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
        fileUploaded = File(request.FILES.get('video_uploaded'))
        userfileUploaded = userfile(
            content=fileUploaded,
            user=request.user
        )
        userfileUploaded.save()
        return HttpResponse(
            '{"errno": 0,"data": {"url": "'+ userfileUploaded.content.url +'"}}',
            content_type='application/json'
        )

#登出用户
def api_user_logout(request):
    logout(request)

'''
通用方法
'''
#获取删除目录时所需要删除的本体和所有子目录，返回列表
def func_getDirsToDelete_list(dir,deleteList):
    deleteList.append(dir)
    if dir.first_child:
        func_getDirsToDelete_list(dir.first_child,deleteList)
    if dir.next_brother:
        func_getDirsToDelete_list(dir.next_brother,deleteList)
    return deleteList