import datetime
import calendar
from dateutil.relativedelta import relativedelta
from django.conf import settings
from django.shortcuts import render,redirect

from CafeFrame.api.common import is_login
from Ledger.models import *

# 主页
def homepage(request):
    if not is_login(request): return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    user = request.user
    current_mode = preference.objects.get(user=user).default_mode
    try: current_mode = request.GET['mode']
    except: pass

    user_preference = preference.objects.get(user=user)
    current_year = int(datetime.datetime.now().strftime('%Y'))
    current_month = int(datetime.datetime.now().strftime('%m'))
    current_month_start = datetime.date(current_year, current_month, 1)
    current_month_end = current_month_start + relativedelta(months=+1)
    current_book = user_preference.default_book
    current_month_budget = None
    try: current_month_budget = budget.objects.get(user=user, year=current_year, month=current_month)
    except: pass

    books = book.objects.filter(user=user).exclude(id=current_book.id)
    bill_classifications = bill_classification.objects.filter(book=current_book)
    bills_day = bill.objects.filter(
            classification__book = current_book,
            create_time__year = datetime.datetime.now().strftime(r'%Y'),
            create_time__month = datetime.datetime.now().strftime(r'%m'),
            create_time__day = datetime.datetime.now().strftime(r'%d')
    ).order_by('-create_time')
    bills_month = bill.objects.filter(classification__book=current_book, create_time__range=(current_month_start,current_month_end)).order_by('-create_time')
    payout_day = 0
    for bill_detail in bills_day:
        if bill_detail.value < 0:
            payout_day += bill_detail.value
    payout_month = 0
    for bill_detail in bills_month:
        if bill_detail.value < 0:
            payout_month += bill_detail.value
    income_day = 0
    for bill_detail in bills_day:
        if bill_detail.value > 0:
            income_day += bill_detail.value
    income_month = 0
    for bill_detail in bills_day:
        if bill_detail.value > 0:
            income_month += bill_detail.value

    context = {
        'current_mode' : current_mode,
        'current_book' : current_book,
        'books' : books,
        'bill_classifications' : bill_classifications,
        'bills_day' : bills_day,
        'bills_month' : bills_month,
        'payout_day' : format(payout_day, '.2f'),
        'income_day' : format(income_day, '.2f'),
        'payout_month' : format(payout_month, '.2f'),
        'income_month' : format(income_month, '.2f'),
    }

    if current_month_budget:
        current_month_budget = int(current_month_budget.budget)
        budget_left_month = float(current_month_budget + payout_month)
        budget_left_month_ratio = budget_left_month / current_month_budget * 100

        current_day_budget = float(
            (current_month_budget + payout_month) / 
            (calendar.monthrange(current_year, current_month)[1] - 
                int(datetime.datetime.now().strftime(r'%d')) + 1
            )
        )
        budget_left_day = float(current_day_budget + payout_day)
        budget_left_day_ratio = budget_left_day / current_day_budget * 100
        
        context['current_month_budget'] = current_month_budget
        context['budget_left_month'] = format(budget_left_month, '.2f')
        context['budget_left_month_ratio'] = int(budget_left_month_ratio)
        context['budget_used_month_ratio'] = 100 - int(budget_left_month_ratio)
        context['current_day_budget'] = format(current_day_budget, '.2f')
        context['budget_left_day'] = format(budget_left_day, '.2f')
        context['budget_left_day_ratio'] = int(budget_left_day_ratio)
        context['budget_used_day_ratio'] = 100 - int(budget_left_day_ratio)
        
    return render(request,'Ledger/homepage/homepage.html',context)