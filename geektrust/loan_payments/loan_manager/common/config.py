import json
from uuid import uuid4
import base64
from django.core import serializers
from .. import models
from django.utils import crypto
from django.core.signing import Signer

failed = "failed"
success = "success"
GET = 'GET'
POST = 'POST'
header = 'HEADER'
app_code = 'g3eK_t7R_#278_s___T'
len_of_uid = 17
X_GEEK_HEADER = 'x-geek-trust-key'
CONTENT_TYPE = "application/json"
NO_OP_ALLOWED = json.dumps({"msg": "operation not allowed", "status": failed})


def getJsonSet(qset):
    data = json.loads(serializers.serialize('json', qset))
    rows = [f['fields'] for f in data]
    return rows


def getBodyFromReq(req):
    return json.loads(req.body.decode('utf-8'))


def getuuid():
    uuid = base64.urlsafe_b64encode(uuid4().bytes).rstrip(b'=').decode('ascii')
    return uuid[0: len_of_uid].__str__()


def getSecretAccessKey():
    return crypto.get_random_string(len_of_uid)


def getSignerObject():
    signer = Signer()
    return signer.sign_object({'key': getSecretAccessKey(), 'app_code': app_code})


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
