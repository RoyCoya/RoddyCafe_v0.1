from django.urls import path
from . import views

'''页面'''
pages = [
	# 主页tab
	path('', views.homepage, name='Ledger_homepage'),
    # 历史tab
	path('history/', views.history, name='Ledger_history'),
    # 个人偏好tab
    path('preference/', views.preference, name='Ledger_preference'),
]

'''接口'''
apis = [
	# 提交收支记录
	path('bill/submit/', views.api_bill_submit, name='api_Ledger_bill_submit'),
]

urlpatterns = pages + apis