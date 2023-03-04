import pytz

from django.http import *
from datetime import datetime
from Ledger.models import *

def submit(request):
    classification_id = int(request.POST['classification_id'])
    remark = request.POST['remark']
    bill_value = 0
    try:
        bill_value = {
            'income' : lambda : float(request.POST['value']),
            'payout' : lambda : float('-' + request.POST['value']),
        }[request.POST['type']]()
    except Exception as e: return HttpResponseBadRequest(e)
    if bill_value != 0:
        print(1)
        bill.objects.create(
            classification = bill_classification.objects.get(id=classification_id),
            value = bill_value,
            create_time = datetime.now(tz=pytz.timezone("Asia/Shanghai")),
            remark = remark,
        )

    return HttpResponse('收支记录提交成功')