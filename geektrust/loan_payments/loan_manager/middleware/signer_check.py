import json
from functools import wraps

from django.shortcuts import HttpResponse as res

from loan_manager.common import utils, field_names


# example of closure, decorator or middleware functions
def check_signer_with_api_type(api_type=None):
    def check_signer(func):
        @wraps(func)
        def func_wrapper(*args, **kwargs):
            req = args[0]
            has_body = req.body.__len__() != 0
            has_signer_key = utils.signer_header_key in req.headers
            signer_key_from_header = ''
            if has_signer_key:
                signer_key_from_header = req.headers[utils.signer_header_key]
            if has_body:
                body = utils.getBodyFromReq(req)

            unsigner = utils.getUnSignerObject(signer_key_from_header)
            subscribed = unsigner[field_names.subscription]
            allow_external_from_db = utils.get_field_values_from_model_object(subscribed, field_names.allow_external) if subscribed != None else False
            allow_crud_internal_from_db = utils.get_field_values_from_model_object(subscribed, field_names.allow_crud_internal) if subscribed != None else False
            is_matched = unsigner[field_names.matched] and subscribed != None
            if api_type == field_names.external:
                allow_to_run = is_matched and allow_external_from_db == True and allow_crud_internal_from_db == False
            elif api_type == field_names.crud:
                allow_to_run = is_matched and allow_external_from_db == False and allow_crud_internal_from_db == True

            msg = {"msg": utils.not_allowed, "status": allow_to_run, "api_type": api_type}
            if allow_to_run == False: return res(json.dumps(msg), content_type=utils.CONTENT_TYPE)
            return func(*args, **kwargs)

        return func_wrapper

    return check_signer