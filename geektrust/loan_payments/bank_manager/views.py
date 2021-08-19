from django.shortcuts import render, HttpResponse as res
from django.http import HttpRequest
from django.views.decorators.csrf import csrf_exempt
from loan_manager.common import utils
import json
from bank_manager import models
from .validations import validate as bankValidations


# Create your views here.
@csrf_exempt
def fn_ADD_BANK(req: HttpRequest):
    if req.method == utils.GET:
        return res(utils.NO_OP_ALLOWED)
    body = utils.getBodyFromReq(req)
    name = body['name']
    inputs = {"name": name}
    flag = True
    validate = bankValidations.validate_input_add_new_bank(inputs)
    if validate['status'] == True:
        try:
            uid = utils.get_uniq_bankid()
            model = models.BANKS(name=name, uid=uid)
            model.save()
            utils.addlog('banks', body)
            success = {
                "msg": f'bank {name} added - {uid}',
                "status": utils.success
            }
        except Exception as ex:
            failed = {
                "msg": f'bank {name} not added',
                "detail": str(ex),
                "status": utils.failed
            }
            flag = False
            utils.adderror('bank error', str(ex))
    else:
        flag = False
        failed = {
            "msg": f'{validate["msg"]}',
            "status": utils.failed
        }

    output = success if flag == True else failed
    return res(json.dumps(output), content_type=utils.CONTENT_TYPE)


@csrf_exempt
def fn_GET_LIST_of_BANKS(req):
    if req.method == utils.POST:
        return res(utils.NO_OP_ALLOWED)
    data = utils.getJsonSet(models.BANKS.objects.only('id', 'name', 'uid', 'when').order_by('id'))
    output = {'data': data}
    utils.addlog('banks', {'bank_fetch':True})
    return res(json.dumps(output), content_type=utils.CONTENT_TYPE)
