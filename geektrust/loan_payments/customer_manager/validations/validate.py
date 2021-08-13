from ..models import CUSTOMERS


def validate_input_add_new_customer(inputs):
    flag = True
    msg = 'all good'
    name = inputs['name']
    if name == '':
        msg = 'name is blank or length is more than 10 characters'
        flag = False
    else:
        try:
            found = CUSTOMERS.objects.get(name=name)
        except CUSTOMERS.DoesNotExist:
            found = None
        if found != None and found.id != None:
            msg = 'record already exists'
            flag = False

    return {"status": flag, "msg": msg}
