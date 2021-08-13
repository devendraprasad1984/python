from django.shortcuts import render, HttpResponse as res
from django.http import HttpRequest
from loan_manager.common import config
from django.views.decorators.csrf import csrf_exempt
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
    output = {"key": key, "signed": sign,
              "msg": f'thanks {name}! for subscribing our apis and saas solutions. you secret key has been mailed to you'
                     f' at {email}. use it in header {config.X_GEEK_HEADER} for accessing our services. this will be valid for next 1 yeae, '
                     f'you have to get it regnerated for further use', "status": config.success}
    return res(json.dumps(output), content_type=config.CONTENT_TYPE)


def gn_GET_SUBSCRIBERS(req: HttpRequest):
    if req.method == config.POST:
        return res(config.NO_OP_ALLOWED)
    return res('here is your list')
