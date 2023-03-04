from django.shortcuts import render
from Ledger.pages import homepage as page_homepage, history as page_history, preference as page_preference
from Ledger.apis import bill as api_bill
# Create your views here.

'''页面'''
# 主页
def homepage(request): return page_homepage.homepage(request)
# 历史记录
def history(request): return page_history.history(request)
# 个人设置
def preference(request): return page_preference.preference(request)

'''接口'''
def api_bill_submit(request): return api_bill.submit(request)

# def api_()