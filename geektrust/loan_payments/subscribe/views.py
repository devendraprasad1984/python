import json

from django.http import HttpRequest
from django.shortcuts import HttpResponse as res
from django.views.decorators.csrf import csrf_exempt
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework_simplejwt import tokens as jwtsimple

from loan_payments import params
from loan_payments.common import utils, field_names, lookup
from . import models
from .validations import validate as subscribe_validator


# Create your views here.
def fn_GET_NEW_TOKEN(req: HttpRequest):
    if req.method == utils.POST:
        return res(utils.NO_OP_ALLOWED)
    key = utils.getSecretAccessKey()
    sign = utils.getSignerObject()
    unsign_check = utils.getUnSignerObject(sign)
    output = {"key": key, "signed": sign, field_names.msg: "here is your secret key, keep it safe", field_names.status: utils.success}
    return res(json.dumps(output), content_type=utils.CONTENT_TYPE)

@csrf_exempt
def fn_CHECK_API_SIGNER(req: HttpRequest):
    if req.method == utils.GET:
        return res(utils.NO_OP_ALLOWED)
    body = utils.getBodyFromReq(req)
    check_flag, msg = lookup.check_field_existence_in_request_body(body, [field_names.signer])
    if check_flag == False: return res(msg, content_type=utils.CONTENT_TYPE)

    sign = body[field_names.signer]
    unsign_check = utils.getUnSignerObject(sign)
    # sign = unsign_check['unsigner']
    matched = unsign_check[field_names.matched]
    key = unsign_check[field_names.key]
    output = {"matched": matched, field_names.msg: "access granted", field_names.status: utils.success}
    return res(json.dumps(output), content_type=utils.CONTENT_TYPE)

@csrf_exempt
@swagger_auto_schema(methods=[params.post_], request_body=params.subscription_req_body, operation_description=params.subscription_req_desc)
@api_view([params.post_])
def fn_SUBSCRIBE(req: HttpRequest):
    if req.method == utils.GET:
        return res(utils.NO_OP_ALLOWED)
    body = utils.getBodyFromReq(req)
    check_flag, msg = lookup.check_field_existence_in_request_body(body, [field_names.name, field_names.email, field_names.type])
    if check_flag == False: return res(msg, content_type=utils.CONTENT_TYPE)

    name = body[field_names.name]
    email = body[field_names.email]
    # allow_external_access = body[field_names.allow_external_access]
    # allow_crud_internal = body[field_names.allow_crud_internal]
    type = body[field_names.type]

    sign, base_object = utils.getSignerObject()
    key = base_object[field_names.key]

    flag = True
    validate = subscribe_validator.validate_input_subscribe(body)
    if validate[field_names.status] == True:
        try:
            model = models.SUBSCRIPTION(
                name=name,
                email=email,
                secret_key=key,
                signer=sign,
                type=type
            )
            model.save()
            utils.addlog(field_names.new_subscription, body)
            success = {
                field_names.msg: {"key": key, "signed": sign,
                                  field_names.msg: f'Thanks {name}! for subscribing our apis and saas solutions. you secret key has been mailed to you'
                               f' at {email}. use it in header {utils.signer_header_key} for accessing our services. this will be valid for next 1 year. '
                               f'You have to get it regnerated for further use', field_names.status: utils.success},
                field_names.status: utils.success
            }
        except Exception as ex:
            failed = {
                field_names.msg: f'subscription for {email} not added. contact admin',
                field_names.detail: str(ex),
                field_names.status: utils.failed
            }
            flag = False
            utils.adderror(field_names.subscription_error, str(ex))
    else:
        flag = False
        failed = {
            field_names.msg: f'{validate["msg"]}',
            field_names.status: utils.failed
        }

    output = success if flag == True else failed
    return res(json.dumps(output), content_type=utils.CONTENT_TYPE)

@swagger_auto_schema(methods=[params.get_], operation_description=params.subscription_list_desc)
@api_view([params.get_])
def gn_GET_SUBSCRIBERS(req: HttpRequest):
    if req.method == utils.POST:
        return res(utils.NO_OP_ALLOWED)
    data = utils.getJsonSet(models.SUBSCRIPTION.objects.only(field_names.id, field_names.name, field_names.email, field_names.secret_key, field_names.signer, field_names.when).order_by(field_names.id))
    output = {'data': data}
    utils.addlog(field_names.subscription, {'subscription list fetch': True})
    return res(json.dumps(output), content_type=utils.CONTENT_TYPE)

# @csrf_exempt
# def fn_ADD_API_USER(req):
#     if req.method == utils.GET:
#         return res(utils.NO_OP_ALLOWED)
#     body = utils.getBodyFromReq(req)
#     check_flag, msg = lookup.check_field_existence_in_request_body(body, [field_names.username, field_names.email, field_names.pwd])
#     if check_flag == False: return res(msg, content_type=utils.CONTENT_TYPE)
#
#     user = body[field_names.username]
#     email = body[field_names.email]
#     pwd = body[field_names.pwd]
#     trace = ''
#     try:
#         user = User.objects.create_user(user, email, pwd)
#         user.save()
#         flag = True
#     except Exception as ex:
#         flag = False
#         trace = str(ex)
#     return res(json.dumps({'status': utils.success if flag else utils.failed, field_names.msg: f"user {user} {'added' if flag else 'not added'}", "trace": trace}), content_type=utils.CONTENT_TYPE)

@csrf_exempt
@swagger_auto_schema(methods=[params.post_], request_body=params.new_jwt_req_body, operation_description=params.new_jwt_req_desc)
@api_view([params.post_])
def fn_JWT_TOKEN_PAIR(req):
    if req.method == utils.GET:
        return res(utils.NO_OP_ALLOWED)
    # pairs=jwtSerialiser.TokenObtainSerializer(jwt_views.TokenObtainPairView.as_view())
    body = utils.getBodyFromReq(req)
    check_flag, msg = lookup.check_field_existence_in_request_body(body, [field_names.user])
    if check_flag == False: return res(msg, content_type=utils.CONTENT_TYPE)

    user = body[field_names.user]
    mytoken = jwtsimple.RefreshToken.for_user(user)
    return res(json.dumps({"refresh": str(mytoken), "access": str(mytoken.access_token)}), content_type=utils.CONTENT_TYPE)
