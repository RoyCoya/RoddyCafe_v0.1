from django.http import *
from django.shortcuts import render,redirect

from AFdian.api import AFdian
from AFdian.models import *

from CafeFrame.api.common import is_login

# 查cookie，没查到提醒登录
def index(request):
    # error_code
    # 200: 成功
    # 403: 该用户没有创建auth_token
    # 404: 有token，读的数据为空
    # 502: 有token，读数据过程出错
    if not is_login(request): return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    
    auth_token = None
    sponsorships = None
    authed = False
    try:
        auth_token = AFD_info.objects.get(user=request.user).token
        authed = True
    except Exception as e: print(e)
    if authed: sponsorships, error_code = AFdian.get_sponsorships(auth_token)
    else: error_code = 403

    context = {
        "sponsorships" : sponsorships,
        "error_code" : error_code,
    }

    return render(request,'AFdian/index.html',context)