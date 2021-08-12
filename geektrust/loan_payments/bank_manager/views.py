from django.shortcuts import render, HttpResponse as res
from django.http import HttpRequest
from django.views.decorators.csrf import csrf_exempt
from geektrust.loan_payments.loan_manager.common import config
import json
# from geektrust.loan_payments.loan_manager import models


# Create your views here.
@csrf_exempt
def fn_ADD_BANK(req: HttpRequest):
    if req.method == 'GET':
        return res(config.NO_OP_ALLOWED)
    uid = config.get_uniq_bankid()
    body = config.getBodyFromReq(req)
    name = body['name']
    # bankModel = models.BANKS
    # bankModel.save(name=name,uid=uid)
    output = {
        "msg": f'bank added - {uid}',
        "name": name,
        "status": config.success
    }
    return res(json.dumps(output), content_type=config.CONTENT_TYPE)
