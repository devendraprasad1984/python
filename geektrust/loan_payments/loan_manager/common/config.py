import json
from uuid import uuid4
import base64
from django.core import serializers

failed = "failed"
success = "success"
GET = 'GET'
POST = 'POST'
header = 'HEADER'
len_of_uid = 17
CONTENT_TYPE = "application/json"
NO_OP_ALLOWED = json.dumps({"msg": "operation not allowed", "status": failed})


def getJsonSet(qset):
    data = json.loads(serializers.serialize('json', qset))
    fieldsData=[f['fields'] for f in data]
    return fieldsData


def getBodyFromReq(req):
    return json.loads(req.body.decode('utf-8'))


def getuuid():
    uuid = base64.urlsafe_b64encode(uuid4().bytes).rstrip(b'=').decode('ascii')
    return uuid[0: len_of_uid].__str__()


def get_uniq_bankid():
    uid = f'bnk{getuuid()}'
    return uid


def get_uniq_customerid():
    uid = f'cst{getuuid()}'
    return uid


def get_uniq_loanid():
    uid = f'ln{getuuid()}'
    return uid
