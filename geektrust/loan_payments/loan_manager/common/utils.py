from bank_manager import models as bank
from customer_manager import models as customer
from subscribe import models as subscriber


def check_bank_exists(name):
    id = -1
    flag = True
    try:
        found = bank.BANKS.objects.get(name=name)
        id = found.id
    except bank.BANKS.DoesNotExist:
        found = None
        if found != None and found.id != None:
            flag = False
    return {"id": id, "name": name, "status": flag}


def check_customer_exists(email):
    id = -1
    name = ''
    flag = True
    try:
        found = customer.CUSTOMERS.objects.get(email=email)
        id = found.id
        name = found.name
        loan_limit = found.loan_limit
    except customer.CUSTOMERS.DoesNotExist:
        found = None
        if found != None and found.id != None:
            flag = False
    return {"id": custid, "name": name, "loan_limit": loan_limit, "status": flag}


def check_subscriber(email):
    id = -1
    name = ''
    flag = True
    try:
        found = subscriber.SUBSCRIPTION.objects.get(email=email)
        id = found.id
        name = found.name
    except subscriber.SUBSCRIPTION.DoesNotExist:
        found = None
        if found != None and found.id != None:
            flag = False
    return {"id": id, "name": name, "status": flag}
