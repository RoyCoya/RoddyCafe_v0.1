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

urlpatterns = [
    path('admin/', admin.site.urls),
    #基础架构：包含主页、个人面板等
    path('', include('CafeFrame.urls')),
    #笔记库
    path('notebook/', include('Notebook.urls')),
    #项目管理与成就网：特殊的笔记。在此app中单独提供特有的一些功能（包括成就网络、项目管理等）
    path('achievementnet/', include('AchievementNet.urls')),
    #生命流：未来（订阅iOS日历，提供预约）、现在（个人当前状态与信息）、过去（根据现在留下的记录）
    path('lifestream/', include('LifeStream.urls')),
    #资源库：供下载的资源
    path('warehouse/', include('Warehouse.urls')),
    #工具库：其他小工具（不需要单独做成app的工具）
    path('lumberroom/', include('LumberRoom.urls')),
]
