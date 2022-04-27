from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from numpy import equal
from .models import notebook_directory, notebook_note, notebook_userfile
from django.urls import reverse
from django.core.files import File
from django.db.models import Q

# Create your views here.

'''
静态页面
'''

#主页
def index(request):
    return render(request,'Notebook/index.html')

#目录->所有目录
def directory(request):
    dirs = notebook_directory.objects.all()
    root_dir = dirs[0]
    context = {
        'root_dir':root_dir
    }
    return render(request,'Notebook/directory/allDirectories.html',context)

#目录->目录内笔记列表详情
def directory_notelist(request,directory_id):
    directory = notebook_directory.objects.get(directory_id=directory_id)
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

#笔记
def note(request,note_id):
    note = notebook_note.objects.get(note_id=note_id)
    context = {
        'note' : note
    }
    return render(request,'Notebook/note/detail.html',context)

#笔记->编辑
def note_edit(request,note_id):
    note = notebook_note.objects.get(note_id=note_id)
    context = {
        'note' : note
    }
    return render(request,'Notebook/note/edit.html',context)

#笔记->新增
def note_new(request,directory_id):
    directory = notebook_directory.objects.get(directory_id=directory_id)
    context = {
        'directory':directory
    }
    return render(request,'Notebook/directory/newNote.html',context)

'''
接口
'''

#删除目录
#TODO：删除后的跳转
def api_directory_delete(request,directory_id):
    directory = notebook_directory.objects.get(directory_id=directory_id)
    directory.delete()
    return HttpResponse('delete directory success')

#新增目录
def api_directory_new_save(request):
    new_directory = notebook_directory(
        directory_name = request.POST['directory_name'],
        directory_discription = request.POST['directory_discription']
    )
    new_directory.save()
    postion = str(request.POST['directory_position']).split('_')
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
            print("#执行：插入为中间目录")
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
    return HttpResponse('directory saved successfully')

#删除笔记
def api_note_delete(request,note_id):
    note = notebook_note.objects.get(note_id=note_id)
    directory = note.note_directory
    note.delete()
    return HttpResponseRedirect(reverse('Notebook_directory_notelist',args=(directory.directory_id,)))

#保存笔记编辑
def api_note_save(request,note_id):
    note = notebook_note.objects.get(note_id=note_id)
    directory = note.note_directory
    note.note_content = request.POST['note_content_edited']
    note.save()
    return HttpResponse('note saved successfully.')

#新增笔记
def api_note_new_save(request,directory_id):
    directory = notebook_directory.objects.get(directory_id=directory_id)
    new_note = notebook_note(
        note_directory=directory,
        note_title=request.POST['note_title'],
        note_content=request.POST['note_content'],
    )
    new_note.save()
    return HttpResponse(new_note.note_id)

#wangeditor上传图片
def api_userfile_upload_img(request):
    fileUploaded = File(request.FILES.get('img_uploaded'))
    userfile = notebook_userfile(userfile_content=fileUploaded)
    userfile.save()
    return HttpResponse(
        '{"errno": 0,"data": {"url": "'+ userfile.userfile_content.url +'","href": "'+ userfile.userfile_content.url +'"}}',
        content_type='application/json'
    )

#wangeditor上传视频
def api_userfile_upload_video(request):
    fileUploaded = File(request.FILES.get('video_uploaded'))
    userfile = notebook_userfile(userfile_content=fileUploaded)
    userfile.save()
    return HttpResponse(
        '{"errno": 0,"data": {"url": "'+ userfile.userfile_content.url +'"}}',
        content_type='application/json'
    )

'''
通用方法
'''