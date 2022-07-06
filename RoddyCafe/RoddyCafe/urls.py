"""RoddyCafe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path
from django.views.static import serve
import django.contrib.auth.urls

djangoURLs = [
    #django自带后台
    path('admin/', admin.site.urls),
    #django自带用户验证模版
    path('accounts/', include('django.contrib.auth.urls')),
]

# 咖啡屋对外的功能
cafe = [
    # 基础架构：店铺门口、店内大厅相关
    path('', include('CafeFrame.urls')),
    # 笔记本
    path('notebook/', include('Notebook.urls')),
]

urlpatterns = djangoURLs + cafe

# 开发时可显示用户文件
if settings.DEBUG:
    urlpatterns += [
        re_path(r'^userfile/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]

