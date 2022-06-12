#登陆检查
def is_login(request):
    if request.user.is_authenticated: return True
    else: return False