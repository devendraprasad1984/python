from ..models import BANKS


def validate_input_add_new_bank(inputs):
    flag = True
    msg = 'all good'
    name = inputs['name']
    if name == '' or len(name) > 10:
        msg = 'name is blank or length is more than 10 characters'
        flag = False
    else:
        try:
            found = BANKS.objects.get(name=name)
        except BANKS.DoesNotExist:
            found = None
        if found != None and found.id != None:
            msg = f'record {name} already exists'
            flag = False

    return {"status": flag, "msg": msg}
