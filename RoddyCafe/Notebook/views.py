import imp
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import notebook_directory, notebook_note, notebook_userfile
from django.urls import reverse
from django.core.files import File

# Create your views here.

'''
静态页面
'''

#主页
def index(request):
    return render(request,'Notebook/index.html')

#目录->所有目录
def directory(request):
    directories = notebook_directory.objects.all()
    context = {
        'Directories':directories
    }
    return render(request,'Notebook/directory/allDirectories.html',context)

#目录->目录内笔记列表详情
def directory_notelist(request,directory_id):
    directory = notebook_directory.objects.get(directory_id=directory_id)
    notes = notebook_note.objects.filter(note_directory=directory)
    context = {
        'directory' : directory,
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
    note = notebook_note(
        note_directory=directory,
        note_title=request.POST['note_title'],
        note_content=request.POST['note_content'],
    )
    note.save()
    return HttpResponse(note.note_id)

#wangeditor上传文件
def api_userfile_upload(request):
    fileUploaded = File(request.FILES.get('wangeditor-uploaded-image'))
    userfile = notebook_userfile(userfile_content=fileUploaded)
    userfile.save()
    return HttpResponse(
        '{"errno": 0,"data": {"url": "'+ userfile.userfile_content.url +'","alt": "图片描述","href": "#"}}',
        content_type='application/json'
    )



'''
通用方法
'''