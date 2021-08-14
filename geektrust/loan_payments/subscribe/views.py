from django.shortcuts import render, HttpResponse as res
from django.http import HttpRequest
from loan_manager.common import config
from django.views.decorators.csrf import csrf_exempt
from .validations import validate as subscribe_validator
from . import models
import json


# Create your views here.
def fn_GET_NEW_TOKEN(req: HttpRequest):
    if req.method == config.POST:
        return res(config.NO_OP_ALLOWED)
    key = config.getSecretAccessKey()
    sign = config.getSignerObject()
    output = {"key": key, "signed": sign, "msg": "here is your secret key, keep it safe", "status": config.success}
    return res(json.dumps(output), content_type=config.CONTENT_TYPE)


@csrf_exempt
def fn_SUBSCRIBE(req: HttpRequest):
    if req.method == config.GET:
        return res(config.NO_OP_ALLOWED)
    body = config.getBodyFromReq(req)
    name = body['name']
    email = body['email']
    key = config.getSecretAccessKey()
    sign = config.getSignerObject()

    flag = True
    validate = subscribe_validator.validate_input_subscribe(body)
    if validate['status'] == True:
        try:
            model = models.SUBSCRIPTION(name=name, email=email, secret_key=key, signer=sign)
            model.save()
            config.addlog('new subscription',body)
            success = {
                "msg": {"key": key, "signed": sign,
                        "msg": f'thanks {name}! for subscribing our apis and saas solutions. you secret key has been mailed to you'
                               f' at {email}. use it in header {config.X_GEEK_HEADER} for accessing our services. this will be valid for next 1 yeae, '
                               f'you have to get it regnerated for further use', "status": config.success},
                "status": config.success
            }
        except Exception as ex:
            failed = {
                "msg": f'subscription for {email} not added. contact admin',
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


def gn_GET_SUBSCRIBERS(req: HttpRequest):
    if req.method == config.POST:
        return res(config.NO_OP_ALLOWED)
    data = config.getJsonSet(models.SUBSCRIPTION.objects.only('id','name','email','secret_key','signer','when').order_by('id'))
    output = {'data': data}
    config.addlog('banks', {'subscription list fetch':True})
    return res(json.dumps(output), content_type=config.CONTENT_TYPE)
