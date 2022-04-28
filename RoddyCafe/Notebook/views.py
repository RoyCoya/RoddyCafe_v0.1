import re
from django.conf import settings
from xmlrpc.client import Boolean
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseForbidden,HttpResponseRedirect
from .models import notebook_directory, notebook_note, notebook_userfile
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
def directory(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
        dirs = notebook_directory.objects.filter(directory_user=request.user)
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
        directory = notebook_directory.objects.get(directory_id=directory_id)
        if request.user != directory.directory_user:
            return HttpResponseForbidden('您无权查看此页面')
        dir = directory
        #拉取所有父目录
        directory_parent = False
        try:
            directory_parent = notebook_directory.objects.get(Q(directory_first_child=directory)|Q(directory_next_brother=directory))
        except Exception as e:
            pass
        parents_directories = []
        while(directory_parent):
            if directory == directory_parent.directory_first_child:
                parents_directories.append(directory_parent)
            directory = directory_parent
            try:
                directory_parent = notebook_directory.objects.get(Q(directory_first_child=directory)|Q(directory_next_brother=directory))
            except Exception as e:
                break
        notes = notebook_note.objects.filter(note_directory=dir).order_by('note_title')
        parents_directories.reverse()
        #拉取所有子目录
        children_directories = []
        try:
            directory = dir
            directory_child = directory.directory_first_child
            while(directory_child):
                children_directories.append(directory_child)
                directory_child = directory_child.directory_next_brother
        except Exception as e:
            pass
        context = {
            'directory' : dir,
            'directory_parents' : parents_directories,
            'directory_children' : children_directories,
            'notes' : notes,
        }
        return render(request,'Notebook/directory/notelist.html',context)

#笔记详情
def note(request,note_id):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
        note = notebook_note.objects.get(note_id=note_id)
        if request.user != note.note_user:
            return HttpResponseForbidden('您无权查看此页面')
        context = {
            'note' : note
        }
        return render(request,'Notebook/note/detail.html',context)

#笔记->编辑
def note_edit(request,note_id):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
        note = notebook_note.objects.get(note_id=note_id)
        if request.user != note.note_user:
            return HttpResponseForbidden('您无权查看此页面')
        context = {
            'note' : note
        }
        return render(request,'Notebook/note/edit.html',context)

#笔记->新增
def note_new(request,directory_id):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
        directory = notebook_directory.objects.get(directory_id=directory_id)
        if request.user != directory.directory_user:
            return HttpResponseForbidden('您无权查看此页面')
        context = {
            'directory':directory
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
        directory = notebook_directory.objects.get(directory_id=directory_id)
        if request.user != directory.directory_user:
            return HttpResponseForbidden('您无权查看此页面')
        parent = notebook_directory.objects.get(Q(directory_first_child=directory)|Q(directory_next_brother=directory))
        isFirstChild = False if parent.directory_first_child != directory else True
        if isFirstChild:
            parent.directory_first_child = directory.directory_next_brother
            parent.save()
            delete_list = [directory]
            if directory.directory_first_child:
                delete_list = func_getDirsToDelete_list(directory.directory_first_child,delete_list)
            for dir in delete_list: dir.delete()
        else:
            parent.directory_next_brother = directory.directory_next_brother
            parent.save()
            delete_list = [directory]
            if directory.directory_first_child:
                delete_list = func_getDirsToDelete_list(directory.directory_first_child,delete_list)
            for dir in delete_list: dir.delete()      
        return HttpResponseRedirect(reverse('Notebook_directory'))

#根目录页面中新增目录
def api_directory_new_save(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
        new_directory = notebook_directory(
            directory_user = request.user,
            directory_name = request.POST['directory_name'],
            directory_discription = request.POST['directory_discription']
        )
        new_directory.save()
        postion = str(request.POST['directory_position']).split('_')
        if len(postion)>1:
            parent = notebook_directory.objects.get(directory_id=postion[1])
            child = None
            if postion[2]:
                child = notebook_directory.objects.get(directory_id=postion[2])
            if child:
                isFirstChild = True if parent.directory_first_child == child else False
                if isFirstChild:
                    inserted_newDir = notebook_directory.objects.get(directory_id=new_directory.directory_id)
                    parent.directory_first_child = inserted_newDir
                    parent.save()
                    inserted_newDir.directory_next_brother = child
                    inserted_newDir.save()
                else:
                    inserted_newDir = notebook_directory.objects.get(directory_id=new_directory.directory_id)
                    parent.directory_next_brother = inserted_newDir
                    parent.save()
                    inserted_newDir.directory_next_brother = child
                    inserted_newDir.save()
            else:
                isFirstChild = True if postion[3] == 'left' else False
                if isFirstChild:
                    inserted_newDir = notebook_directory.objects.get(directory_id=new_directory.directory_id)
                    parent.directory_first_child = inserted_newDir
                    parent.save()
                else:
                    inserted_newDir = notebook_directory.objects.get(directory_id=new_directory.directory_id)
                    parent.directory_next_brother = inserted_newDir
                    parent.save()
        else:
            dirs = notebook_directory.objects.filter(directory_user=request.user)
            inserted_newDir = notebook_directory.objects.get(directory_id=new_directory.directory_id)
            root_dir = dirs[0]
            root_dir.directory_first_child = inserted_newDir
            root_dir.save()
        return HttpResponse('new directory created successfully')

#删除笔记
def api_note_delete(request,note_id):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
        note = notebook_note.objects.get(note_id=note_id)
        if request.user != note.note_user:
            return HttpResponseForbidden('您无权查看此页面')
        directory = note.note_directory
        note.delete()
        return HttpResponseRedirect(reverse('Notebook_directory_notelist',args=(directory.directory_id,)))

#保存笔记编辑
def api_note_save(request,note_id):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
        note = notebook_note.objects.get(note_id=note_id)
        if request.user != note.note_user:
            return HttpResponseForbidden('您无权查看此页面')
        directory = note.note_directory
        note.note_content = request.POST['note_content_edited']
        note.save()
        return HttpResponse('note saved successfully.')

#新增笔记
def api_note_new_save(request,directory_id):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
        directory = notebook_directory.objects.get(directory_id=directory_id)
        if request.user != directory.directory_user:
            return HttpResponseForbidden('您无权查看此页面')
        new_note = notebook_note(
            note_directory=directory,
            note_user=request.user,
            note_title=request.POST['note_title'],
            note_content=request.POST['note_content'],
        )
        new_note.save()
        return HttpResponse(new_note.note_id)

#wangeditor上传图片
def api_userfile_upload_img(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
        fileUploaded = File(request.FILES.get('img_uploaded'))
        userfile = notebook_userfile(userfile_content=fileUploaded,userfile_user=request.user)
        userfile.save()
        return HttpResponse(
            '{"errno": 0,"data": {"url": "'+ userfile.userfile_content.url +'","href": "'+ userfile.userfile_content.url +'"}}',
            content_type='application/json'
        )

#wangeditor上传视频
def api_userfile_upload_video(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
        fileUploaded = File(request.FILES.get('video_uploaded'))
        userfile = notebook_userfile(userfile_content=fileUploaded,userfile_user=request.user)
        userfile.save()
        return HttpResponse(
            '{"errno": 0,"data": {"url": "'+ userfile.userfile_content.url +'"}}',
            content_type='application/json'
        )

#登出用户
def api_user_logout(request):
    logout(request)

'''
通用方法
'''
def func_getDirsToDelete_list(dir,deleteList):
    deleteList.append(dir)
    if dir.directory_first_child:
        func_getDirsToDelete_list(dir.directory_first_child,deleteList)
    if dir.directory_next_brother:
        func_getDirsToDelete_list(dir.directory_next_brother,deleteList)
    return deleteList