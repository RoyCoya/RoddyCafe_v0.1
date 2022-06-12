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
    # 仓库（资源库，大厅左转）：提供对外开放的下载资源
    path('warehouse/', include('Warehouse.urls')),
    # 杂物间：其他小工具（不需要单独做成app的工具）
    path('lumberroom/', include('LumberRoom.urls')),
]

# 咖啡屋对内（我自己手动添加的用户白名单）的功能
employeeRoom = [
    # 生命流：未来（订阅iOS日历，提供预约）、现在（个人当前状态与信息）、过去（根据现在留下的记录）。
    path('lifestream/', include('LifeStream.urls')),
    # 计划与项目：计划管理、项目管理。与“生命流”联合使用，可快速添加生命流中的事项
    # TODO:计划与项目
    # 笔记本
    path('notebook/', include('Notebook.urls')),
    # 成就树：安插在员工界面的“我的”（profile）中，与“计划与项目”联合使用。当完成指定的计划和项目后，达成成就。该内容可对外展示
    path('achievementnet/', include('AchievementNet.urls')),
]

urlpatterns = djangoURLs + cafe + employeeRoom

# 开发时可显示用户文件
if settings.DEBUG:
    urlpatterns += [
        re_path(r'^userfile/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]

