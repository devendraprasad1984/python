from ..models import SUBSCRIPTION


def validate_input_subscribe(inputs):
    flag = True
    msg = 'all good'
    name = inputs['name']
    email = inputs['email']
    if name == '' or email == '':
        msg = f'invalid input'
        flag = False
    else:
        try:
            found = SUBSCRIPTION.objects.get(email=email)
        except SUBSCRIPTION.DoesNotExist:
            found = None
        if found != None and found.id != None:
            msg = f'subscription record for {name} - {email} already exists'
            flag = False

    return {"status": flag, "msg": msg}
