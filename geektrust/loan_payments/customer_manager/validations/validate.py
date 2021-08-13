from ..models import CUSTOMERS


def validate_input_add_new_customer(inputs):
    flag = True
    msg = 'all good'
    email = inputs['email']
    if email == '':
        msg = f'{email} is blank'
        flag = False
    else:
        try:
            found = CUSTOMERS.objects.get(email=email)
        except CUSTOMERS.DoesNotExist:
            found = None
        if found != None and found.id != None:
            msg = 'record already exists'
            flag = False

    return {"status": flag, "msg": msg}
