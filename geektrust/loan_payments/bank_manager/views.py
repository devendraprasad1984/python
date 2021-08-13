from django.shortcuts import render, HttpResponse as res
from django.http import HttpRequest
from django.views.decorators.csrf import csrf_exempt
from loan_manager.common import config
import json
from bank_manager import models
from .validations import validate as bankValidations


# Create your views here.
@csrf_exempt
def fn_ADD_BANK(req: HttpRequest):
    if req.method == config.GET:
        return res(config.NO_OP_ALLOWED)
    body = config.getBodyFromReq(req)
    name = body['name']
    inputs = {"name": name}
    flag = True
    validate = bankValidations.validate_input_add_new_bank(inputs)
    if validate['status'] == True:
        try:
            uid = config.get_uniq_bankid()
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
    else:
        flag = False
        failed = {
            "msg": f'{validate["msg"]}',
            "status": config.failed
        }

    output = success if flag == True else failed
    return res(json.dumps(output), content_type=config.CONTENT_TYPE)


@csrf_exempt
def fn_GET_LIST_of_BANKS(req):
    if req.method == config.POST:
        return res(config.NO_OP_ALLOWED)
    data = config.getJsonSet(models.BANKS.objects.only('id','name','uid','when').order_by('id'))
    output = {'data': data}
    return res(json.dumps(output), content_type=config.CONTENT_TYPE)
