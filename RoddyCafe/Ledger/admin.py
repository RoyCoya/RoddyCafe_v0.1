from django.contrib import admin
from .models import *

# 账本
class admin_book(admin.ModelAdmin):
	list_display = [
        'id',
		'name',
        'user',
]
admin.site.register(book,admin_book)

# 账单分类
class admin_bill_classification(admin.ModelAdmin):
	list_display = [
		'id',
		'name',
        'book',
]
admin.site.register(bill_classification, admin_bill_classification)

# 收支记录
class admin_bill(admin.ModelAdmin):
	list_display = [
		'id',
        'classification',
        'value',
        'create_time',
        'remark',
    ]
admin.site.register(bill, admin_bill)

# 每月预算
class admin_budget(admin.ModelAdmin):
	list_display = [
		'id',
		'user',
		'year',
		'month',
		'budget',
    ]
admin.site.register(budget,admin_budget)

# 用户偏好
class admin_preference(admin.ModelAdmin):
	list_display = [
		'id',
        'user',
        'default_book',
]
admin.site.register(preference, admin_preference)