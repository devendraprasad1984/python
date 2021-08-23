import json
from functools import wraps

from django.shortcuts import HttpResponse as res

from loan_manager.common import utils, field_names


# example of closure, decorator or middleware functions
def check_signer(func):
    @wraps(func)
    def func_wrapper(*args, **kwargs):
        body = {}
        req = args[0]
        has_body = req.body.__len__() != 0
        has_signer_key = utils.signer_header_key in req.headers
        signer_key_from_header = ''
        if has_signer_key:
            signer_key_from_header = req.headers[utils.signer_header_key]
        if has_body:
            body = utils.getBodyFromReq(req)

        unsign_check = utils.getUnSignerObject(signer_key_from_header)
        allow_to_run = unsign_check[field_names.matched]
        if allow_to_run == False: return res(json.dumps(unsign_check), content_type=utils.CONTENT_TYPE)
        return func(*args, **kwargs)

    return func_wrapper
