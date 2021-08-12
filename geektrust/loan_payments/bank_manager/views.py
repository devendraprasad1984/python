from django.shortcuts import render, HttpResponse as res
from django.http import HttpRequest
from django.views.decorators.csrf import csrf_exempt
from loan_manager.common import config
import json
from loan_manager import models


# Create your views here.
@csrf_exempt
def fn_ADD_BANK(req: HttpRequest):
    if req.method == 'GET':
        return res(config.NO_OP_ALLOWED)
    body = config.getBodyFromReq(req)
    name = body['name']
    uid = config.get_uniq_bankid()
    success = {}
    failed = {}
    flag = True
    try:
        model = models.BANKS(name=name, uid=uid)
        model.save()
        success = {
            "msg": f'bank {name} added - {uid}',
            "status": config.success
        }
    except Exception as ex:
        failed = {
            "msg": f'bank {name} not added',
            "detail": str(ex),
            "status": config.failed
        }
        flag = False

    output = success if flag == True else failed
    return res(json.dumps(output), content_type=config.CONTENT_TYPE)
