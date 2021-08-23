from ..models import CUSTOMERS
from loan_manager.common import lookup


def validate_input_add_new_customer(inputs):
    flag = True
    msg = 'all good'
    name = inputs['name']
    email = inputs['email']
    age = inputs['age']
    limit = inputs['limit']
    if name == '' or email == '' or str(age).isnumeric() == False or str(limit).isnumeric() == False:
        msg = f'name/email is blank or invalid age/limit'
        flag = False
    else:
        obj = lookup.check_customer_exists(email=email)
        if obj['id'] != -1:
            msg = f"record {email} already exists"
            flag = False

    return {"status": flag, "msg": msg}
