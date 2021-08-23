import json

from django.shortcuts import HttpResponse as res
from django.views.decorators.csrf import csrf_exempt

from customer_manager import models
from loan_manager.common import utils, field_names, lookup
from .validations import validate as customerValidations


# Create your views here.
@csrf_exempt
@utils.manager_check_signer_middleware()
def fn_ADD_CUSTOMER(req):
    if req.method == 'GET':
        return res(utils.NO_OP_ALLOWED)

    body = utils.getBodyFromReq(req)
    check_flag, msg = lookup.check_field_existence_in_request_body(body, [field_names.name, field_names.age, field_names.email, field_names.loan_limit])
    if check_flag == False: return res(msg, content_type=utils.CONTENT_TYPE)

    name = body[field_names.name]
    age = body[field_names.age]
    email = body[field_names.email]
    loan_limit = body[field_names.loan_limit]
    flag = True
    validate = customerValidations.validate_input_add_new_customer(body)
    if validate[field_names.status] == True:
        try:
            uid = utils.get_uniq_customerid()
            model = models.CUSTOMERS(
                name=name,
                uid=uid,
                age=age,
                email=email,
                loan_limit=loan_limit
            )
            model.save()
            utils.addlog(field_names.customer, body)
            success = {
                "msg": f'customer {name}, {email}, {age} yrs, having loan {loan_limit} added - {uid}',
                "status": utils.success
            }
        except Exception as ex:
            failed = {
                "msg": f'customer {name} {email} not added',
                "detail": str(ex),
                "status": utils.failed
            }
            flag = False
            utils.adderror('customer error', str(ex))
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
def fn_GET_LIST_of_CUSTOMERS(req, id=None):
    if req.method == utils.POST:
        return res(utils.NO_OP_ALLOWED)
    output = lookup.run_customer_loan_query(**{"id": id})
    utils.addlog(field_names.customer, {'customer_fetch': True})
    return res(json.dumps(output), content_type=utils.CONTENT_TYPE)

@csrf_exempt
@utils.manager_check_signer_middleware()
def fn_GET_CUSTOMER_LOAN(req, loan_ref=None):
    if req.method == utils.POST:
        return res(utils.NO_OP_ALLOWED)
    output = lookup.run_customer_loan_query(**{"loan_ref": loan_ref})
    utils.addlog(field_names.customer_with_loan, {'customer_fetch_loan_ref': True})
    return res(json.dumps(output), content_type=utils.CONTENT_TYPE)
