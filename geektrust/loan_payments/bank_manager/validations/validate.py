from ..models import BANKS
from loan_manager.common import lookup

def validate_input_add_new_bank(inputs):
    flag = True
    msg = 'all good'
    name = inputs['name']
    if name == '' or len(name) > 10:
        msg = 'name is blank or length is more than 10 characters'
        flag = False
    else:
        obj = lookup.check_bank_exists(name=name)
        if obj['id'] != -1:
            msg = f"record {name} already exists"
            flag = False

    return {"status": flag, "msg": msg}
