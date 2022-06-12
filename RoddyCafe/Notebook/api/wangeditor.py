'''wangeditor操作'''

from django.core.files import File
from django.conf import settings
from django.shortcuts import redirect
from django.http import *

from Notebook.models import *
from CafeFrame.api.common import is_login

# wangeditor上传图片
def upload_img(request):
    if not is_login(request): return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    
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

# wangeditor上传视频
def upload_video(request):
    if not is_login(request): return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

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
