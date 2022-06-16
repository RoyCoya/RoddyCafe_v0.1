'''wangeditor操作'''

from django.core.files import File
from django.conf import settings
from django.shortcuts import redirect
from django.http import *

from Notebook.models import *
from CafeFrame.api.common import is_login

# wangeditor上传图片
def upload_img(request, note_id):
    if not is_login(request): return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    
    fileUploaded = File(request.FILES.get('img_uploaded'))
    note_with_file = note.objects.get(id=note_id)
    note_file_uploaded = note_file(
        note=note_with_file,
        file=fileUploaded,
    )
    note_file_uploaded.save()
    
    return HttpResponse(
        '{"errno": 0,"data": {"url": "'+ note_file_uploaded.file.url +'","href": "'+ note_file_uploaded.file.url +'"}}',
        content_type='application/json'
    )

# wangeditor上传视频
def upload_video(request, note_id):
    if not is_login(request): return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

    fileUploaded = File(request.FILES.get('video_uploaded'))
    note_with_file = note.objects.get(id=note_id)
    note_file_uploaded = note_file(
        note=note_with_file,
        file=fileUploaded,
    )
    note_file_uploaded.save()
    
    return HttpResponse(
        '{"errno": 0,"data": {"url": "'+ note_file_uploaded.file.url +'"}}',
        content_type='application/json'
    )
