from ..models import LOANS


def validate_input_add_new_loan(inputs):
    flag = True
    msg = 'all good'
    name = inputs['name']
    email = inputs['email']
    age = inputs['age']
    limit = inputs['limit']
    if name == '' or email == '' or str(age).isnumeric() == False or str(limit).isnumeric() == False:
        msg = f'invalid input'
        flag = False

    return {field_names.status: flag, field_names.msg: msg}
