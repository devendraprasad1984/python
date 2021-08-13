from django.shortcuts import render, HttpResponse as res
from django.views.decorators.csrf import csrf_exempt
from loan_manager.common import config
from customer_manager import models
import json
from .validations import validate as customerValidations


# Create your views here.
@csrf_exempt
def fn_ADD_CUSTOMER(req):
    if req.method == 'GET':
        return res(config.NO_OP_ALLOWED)

    body = config.getBodyFromReq(req)
    name = body['name']
    age = body['age']
    email = body['email']
    loan_limit = body['loan_limit']
    inputs = {"name": name, "email": email, "age": age, "limit": loan_limit}
    flag = True
    validate = customerValidations.validate_input_add_new_customer(inputs)
    if validate['status'] == True:
        try:
            uid = config.get_uniq_bankid()
            model = models.CUSTOMERS(
                name=name,
                uid=uid,
                age=age,
                email=email,
                loan_limit=loan_limit
            )
            model.save()
            config.addlog('customer',body)
            success = {
                "msg": f'customer {name}, {email}, {age} yrs, having loan {loan_limit} added - {uid}',
                "status": config.success
            }
        except Exception as ex:
            failed = {
                "msg": f'customer {name} {email} not added',
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
def fn_GET_LIST_of_CUSTOMERS(req):
    if req.method == config.POST:
        return res(config.NO_OP_ALLOWED)
    data = config.getJsonSet(models.CUSTOMERS.objects.only('id','name','uid','age','loan_limit','when').order_by('id'))
    output = {'data': data}
    config.addlog('customer',{'customer_fetch':True})
    return res(json.dumps(output), content_type=config.CONTENT_TYPE)
