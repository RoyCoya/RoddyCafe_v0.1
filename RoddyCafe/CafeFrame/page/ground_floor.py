from django.shortcuts import render, redirect
from django.conf import settings

from CafeFrame.models import masturbation

# 大厅
def lobby(request):
    mastur_records = masturbation.objects.filter(name="Rocky").order_by("-createDate")
    latest_mastur = mastur_records.first()
    context = {
        "mastur_records" : mastur_records,
        "latest_mastur" : latest_mastur,
    }
    return render(request,'CafeFrame/ground_floor/lobby/lobby.html', context)