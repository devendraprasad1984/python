from django.shortcuts import render, HttpResponse as res
from django.http import HttpRequest
from django.views.decorators.csrf import csrf_exempt
from geektrust.loan_payments.loan_manager.common import config
import json


# Create your views here.
@csrf_exempt
def fn_ADD_BANK(req: HttpRequest):
    if req.method == 'GET':
        return res(config.NO_OP_ALLOWED)
    uid = config.get_uniq_bankid()
    body = config.getBodyFromReq(req)
    name = body['name']
    output = {
        "msg": f'bank added - {uid}',
        "name": name
    }
    return res(json.dumps(output), content_type=config.CONTENT_TYPE)
