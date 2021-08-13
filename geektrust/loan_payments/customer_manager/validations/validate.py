from ..models import CUSTOMERS


def validate_input_add_new_customer(inputs):
    flag = True
    msg = 'all good'
    name = inputs['name']
    email = inputs['email']
    age = inputs['age']
    limit = inputs['limit']
    if name == '' or email == '' or age.isnumeric() == False or limit.isnumeric() == False:
        msg = f'name/email is blank or invalid age/limit'
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
