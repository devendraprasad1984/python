from django.shortcuts import render, HttpResponse as res
from django.http import HttpRequest
from loan_manager.common import config
from django.views.decorators.csrf import csrf_exempt
from .validations import validate as subscribe_validator
from . import models
import json
from rest_framework_simplejwt import views as jwt_views, tokens as jwtsimple
from django.contrib.auth.models import User


# Create your views here.
def fn_GET_NEW_TOKEN(req: HttpRequest):
    if req.method == config.POST:
        return res(config.NO_OP_ALLOWED)
    key = config.getSecretAccessKey()
    sign = config.getSignerObject()
    unsign_check = config.getUnSignerObject(sign)
    output = {"key": key, "signed": sign, "msg": "here is your secret key, keep it safe", "status": config.success}
    return res(json.dumps(output), content_type=config.CONTENT_TYPE)


@csrf_exempt
def fn_CHECK_API_SIGNER(req: HttpRequest):
    if req.method == config.GET:
        return res(config.NO_OP_ALLOWED)
    body = config.getBodyFromReq(req)
    sign = body['signer']
    unsign_check = config.getUnSignerObject(sign)
    # sign = unsign_check['unsigner']
    matched = unsign_check['matched']
    key = unsign_check['key']
    output = {"matched": matched, "msg": "access granted", "status": config.success}
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
            config.addlog('new subscription', body)
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
            config.adderror('subscription error',str(ex))
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
    data = config.getJsonSet(models.SUBSCRIPTION.objects.only('id', 'name', 'email', 'secret_key', 'signer', 'when').order_by('id'))
    output = {'data': data}
    config.addlog('banks', {'subscription list fetch': True})
    return res(json.dumps(output), content_type=config.CONTENT_TYPE)


@csrf_exempt
def fn_ADD_API_USER(req):
    if req.method == config.GET:
        return res(config.NO_OP_ALLOWED)
    body = config.getBodyFromReq(req)
    user = body['username']
    email = body['email']
    pwd = body['pwd']
    trace=''
    try:
        user = User.objects.create_user(user, email, pwd)
        user.save()
        flag = True
    except Exception as ex:
        flag = False
        trace = str(ex)
    return res(json.dumps({'status': config.success if flag else config.failed, "msg": f"user {user} {'added' if flag else 'not added'}", "trace": trace}), content_type=config.CONTENT_TYPE)


@csrf_exempt
def fn_JWT_TOKEN_PAIR(req):
    if req.method == config.GET:
        return res(config.NO_OP_ALLOWED)
    # pairs=jwtSerialiser.TokenObtainSerializer(jwt_views.TokenObtainPairView.as_view())
    body = config.getBodyFromReq(req)
    user = body['user']
    mytoken = jwtsimple.RefreshToken.for_user(user)
    return res(json.dumps({"refresh": str(mytoken), "access": str(mytoken.access_token)}), content_type=config.CONTENT_TYPE)
