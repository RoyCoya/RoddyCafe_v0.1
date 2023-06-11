from django.http import *
from django.shortcuts import render

from AFdian.api import AFdian

# 查cookie，没查到提醒登录
def index(request):
    # error_code
    # 200: 成功
    # 403: cookie里没auth_token
    # 404: 有token，读的数据为空
    # 502: 有token，读数据过程出错
    auth_token = None
    sponsorships = None
    authed = False
    try:
        auth_token = request.COOKIES['AFdian_auth_token']
        authed = True
    except: pass
    if authed: sponsorships, error_code = AFdian.get_sponsorships(auth_token)
    else: error_code = 403

    context = {
        "sponsorships" : sponsorships,
        "error_code" : error_code,
    }

    return render(request,'AFdian/index.html',context)