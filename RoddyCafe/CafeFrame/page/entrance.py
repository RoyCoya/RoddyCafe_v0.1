from django.shortcuts import render

# 门口
def doorway(request):
    return render(request,'CafeFrame/entrance/doorway.html')