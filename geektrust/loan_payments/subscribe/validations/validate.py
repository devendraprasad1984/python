from loan_manager.common import utils


def validate_input_subscribe(inputs):
    flag = True
    msg = 'all good'
    name = inputs['name']
    email = inputs['email']
    if name == '' or email == '':
        msg = f'invalid input'
        flag = False
    else:
        obj = utils.check_subscriber(email)
        if obj['id'] != -1:
            msg = f"record {email} already exists"
            flag = False

    return {"status": flag, "msg": msg}
