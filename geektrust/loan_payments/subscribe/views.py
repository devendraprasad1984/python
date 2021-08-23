import json

from django.contrib.auth.models import User
from django.http import HttpRequest
from django.shortcuts import HttpResponse as res
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt import tokens as jwtsimple

from loan_manager.common import utils, field_names
from . import models
from .validations import validate as subscribe_validator


# Create your views here.
def fn_GET_NEW_TOKEN(req: HttpRequest):
    if req.method == utils.POST:
        return res(utils.NO_OP_ALLOWED)
    key = utils.getSecretAccessKey()
    sign = utils.getSignerObject()
    unsign_check = utils.getUnSignerObject(sign)
    output = {"key": key, "signed": sign, "msg": "here is your secret key, keep it safe", "status": utils.success}
    return res(json.dumps(output), content_type=utils.CONTENT_TYPE)

@csrf_exempt
def fn_CHECK_API_SIGNER(req: HttpRequest):
    if req.method == utils.GET:
        return res(utils.NO_OP_ALLOWED)
    body = utils.getBodyFromReq(req)
    sign = body[field_names.signer]
    unsign_check = utils.getUnSignerObject(sign)
    # sign = unsign_check['unsigner']
    matched = unsign_check[field_names.matched]
    key = unsign_check[field_names.key]
    output = {"matched": matched, "msg": "access granted", "status": utils.success}
    return res(json.dumps(output), content_type=utils.CONTENT_TYPE)

@csrf_exempt
def fn_SUBSCRIBE(req: HttpRequest):
    if req.method == utils.GET:
        return res(utils.NO_OP_ALLOWED)
    body = utils.getBodyFromReq(req)
    name = body[field_names.name]
    email = body[field_names.email]
    key = utils.getSecretAccessKey()
    sign = utils.getSignerObject()

    flag = True
    validate = subscribe_validator.validate_input_subscribe(body)
    if validate[field_names.status] == True:
        try:
            model = models.SUBSCRIPTION(name=name, email=email, secret_key=key, signer=sign)
            model.save()
            utils.addlog(field_names.new_subscription, body)
            success = {
                "msg": {"key": key, "signed": sign,
                        "msg": f'Thanks {name}! for subscribing our apis and saas solutions. you secret key has been mailed to you'
                               f' at {email}. use it in header {utils.X_GEEK_HEADER} for accessing our services. this will be valid for next 1 year. '
                               f'You have to get it regnerated for further use', "status": utils.success},
                "status": utils.success
            }
        except Exception as ex:
            failed = {
                "msg": f'subscription for {email} not added. contact admin',
                "detail": str(ex),
                "status": utils.failed
            }
            flag = False
            utils.adderror(field_names.subscription_error, str(ex))
    else:
        flag = False
        failed = {
            "msg": f'{validate["msg"]}',
            "status": utils.failed
        }

    output = success if flag == True else failed
    return res(json.dumps(output), content_type=utils.CONTENT_TYPE)

def gn_GET_SUBSCRIBERS(req: HttpRequest):
    if req.method == utils.POST:
        return res(utils.NO_OP_ALLOWED)
    data = utils.getJsonSet(models.SUBSCRIPTION.objects.only(field_names.id, field_names.name, field_names.email, field_names.secret_key, field_names.signer, field_names.when).order_by(field_names.id))
    output = {'data': data}
    utils.addlog(field_names.banks, {'subscription list fetch': True})
    return res(json.dumps(output), content_type=utils.CONTENT_TYPE)

@csrf_exempt
def fn_ADD_API_USER(req):
    if req.method == utils.GET:
        return res(utils.NO_OP_ALLOWED)
    body = utils.getBodyFromReq(req)
    user = body[field_names.username]
    email = body[field_names.email]
    pwd = body[field_names.pwd]
    trace = ''
    try:
        user = User.objects.create_user(user, email, pwd)
        user.save()
        flag = True
    except Exception as ex:
        flag = False
        trace = str(ex)
    return res(json.dumps({'status': utils.success if flag else utils.failed, "msg": f"user {user} {'added' if flag else 'not added'}", "trace": trace}), content_type=utils.CONTENT_TYPE)

@csrf_exempt
def fn_JWT_TOKEN_PAIR(req):
    if req.method == utils.GET:
        return res(utils.NO_OP_ALLOWED)
    # pairs=jwtSerialiser.TokenObtainSerializer(jwt_views.TokenObtainPairView.as_view())
    body = utils.getBodyFromReq(req)
    user = body[field_names.user]
    mytoken = jwtsimple.RefreshToken.for_user(user)
    return res(json.dumps({"refresh": str(mytoken), "access": str(mytoken.access_token)}), content_type=utils.CONTENT_TYPE)
