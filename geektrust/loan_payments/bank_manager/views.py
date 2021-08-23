import json

from django.http import HttpRequest
from django.shortcuts import HttpResponse as res
from django.views.decorators.csrf import csrf_exempt

from bank_manager import models
from loan_manager.common import utils, field_names, lookup
from .validations import validate as bankValidations


# Create your views here.
@csrf_exempt
@utils.manager_check_signer_middleware()
def fn_ADD_BANK(req: HttpRequest):
    if req.method == utils.GET:
        return res(utils.NO_OP_ALLOWED)
    body = utils.getBodyFromReq(req)
    check_flag, msg = lookup.check_field_existence_in_request_body(body, [field_names.name])
    if check_flag == False: return res(msg, content_type=utils.CONTENT_TYPE)

    name = body[field_names.name]
    flag = True
    validate = bankValidations.validate_input_add_new_bank(body)
    if validate[field_names.status] == True:
        try:
            uid = utils.get_uniq_bankid()
            model = models.BANKS(name=name, uid=uid)
            model.save()
            utils.addlog(field_names.banks, body)
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
            "msg": f'{validate[field_names.msg]}',
            "status": utils.failed
        }

    output = success if flag == True else failed
    return res(json.dumps(output), content_type=utils.CONTENT_TYPE)

@csrf_exempt
@utils.manager_check_signer_middleware()
def fn_GET_LIST_of_BANKS(req):
    if req.method == utils.POST:
        return res(utils.NO_OP_ALLOWED)
    data = utils.getJsonSet(models.BANKS.objects.only(field_names.id, field_names.name, field_names.uid, field_names.when).order_by(field_names.id))
    output = {'data': data}
    utils.addlog(field_names.banks, {'bank_fetch': True})
    return res(json.dumps(output), content_type=utils.CONTENT_TYPE)
