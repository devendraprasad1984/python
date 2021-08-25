import base64
import json
from uuid import uuid4

from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.core.signing import Signer
from django.utils import crypto

from loan_manager import models
from ..common import lookup, field_names
from ..middleware import signer_check


failed = "failed"
success = "success"
GET = 'GET'
POST = 'POST'
header = 'HEADER'
signer_header_key = 'geek-signer'
x_csrf_key = 'X-CSRFToken'
app_code = 'g3eK_t7R_#278_s___T'
len_of_uid = 17
CONTENT_TYPE = "application/json"
not_allowed = 'operation not allowed or signer or jwt not verified or borrower mail not matched'
NO_OP_ALLOWED = json.dumps({field_names.msg: not_allowed, field_names.status: failed})
MISSING_FIELD_MSG = {field_names.msg: "some input values are missing or left blank. ", field_names.status: failed}


def getSum(object, field):
    sum = 0
    num_list = [float(x[field]) for x in object.values()]
    for val in num_list:
        sum += val.real
    return float(sum)


def getSumFromJsonConverted(object, field):
    return sum([float(x[field]) if x[field] != None else 0 for x in object])


def getList(ds):
    return list(ds.values())


def get_field_values_from_model_object(object, field):
    return getattr(object, field)


def getJsonSet(qset):
    data = json.loads(serializers.serialize('json', qset))
    rows = [f['fields'] for f in data]
    return rows


def jsonEncode(obj):
    return json.loads(json.dumps(obj, cls=DjangoJSONEncoder))


def getBodyFromReq(req):
    return json.loads(req.body.decode('utf-8'))


def getuuid():
    uuid = base64.urlsafe_b64encode(uuid4().bytes).rstrip(b'=').decode('ascii')
    return uuid[0: len_of_uid].__str__()


def getSecretAccessKey():
    return crypto.get_random_string(len_of_uid)


def getSignerObject():
    signer = Signer()
    object = {field_names.key: getSecretAccessKey(), field_names.app_code: app_code}
    signed_object = signer.sign_object(object)
    return signed_object, object


def getUnSignerObject(signObj):
    signer = Signer()
    matched = decoded = False
    key = not_allowed
    subscription = None
    try:
        unsignedObj = signer.unsign_object(signObj)
        decoded = True
    except Exception as ex:
        decoded = False

    if decoded == True:
        key = unsignedObj[field_names.key]
        subcription_object = lookup.check_subscriber(secret_key=key)
        subscription = subcription_object[field_names.object]
        matched = unsignedObj[field_names.app_code] == app_code
    return {field_names.key: key, field_names.matched: matched, field_names.subscription: subscription}


def getUnsigned(signkey):
    signer = Signer()
    return signer.unsign_object(signkey)


def get_uniq_bankid():
    uid = f'bnk{getuuid()}'
    return uid


def get_uniq_customerid():
    uid = f'cst{getuuid()}'
    return uid


def get_uniq_loanid():
    uid = f'ln{getuuid()}'
    return uid


def addlog(type, logObj):
    try:
        dblog = models.QUERY_LOG(
            type=type,
            log=json.dumps(logObj)
        )
        dblog.save()
        return True
    except Exception as ex:
        return str(ex)


def adderror(type, trace):
    addlog(type, {field_names.error: trace})


# returning middleware decorator function with parameter to deal with external api type or having CRUD access to do operations
def external_check_signer_middleware():
    return signer_check.check_signer_with_api_type(api_type=field_names.external)


def crud_check_signer_middleware():
    return signer_check.check_signer_with_api_type(api_type=field_names.crud)


def manager_check_signer_middleware():
    return signer_check.check_signer_with_api_type(api_type=field_names.manager)


def borrower_check_signer_middleware():
    return signer_check.check_signer_with_api_type(api_type=field_names.borrower)
