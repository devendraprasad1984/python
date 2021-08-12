from django.shortcuts import render, HttpResponse as res
from django.views.decorators.csrf import csrf_exempt
from loan_manager.common import config
import json


# Create your views here.
@csrf_exempt
def fn_ADD_CUSTOMER(req):
    if req.method == 'GET':
        return res(config.NO_OP_ALLOWED)
    uid = config.get_uniq_customerid()
    body = config.getBodyFromReq(req)
    name = body['name']
    age = body['age']
    loan_limit = body['loan_limit']
    output = {
        "msg": f'customer {name}, {age} yrs, having loan {loan_limit} added - {uid}',
        "status": config.success
    }
    return res(json.dumps(output), content_type=config.CONTENT_TYPE)
