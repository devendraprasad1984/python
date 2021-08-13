from bank_manager import models as bank
from customer_manager import models as customer
from . import config


def get_bank_id(name):
    bankid = -1
    flag = True
    try:
        found = bank.BANKS.objects.get(name=name)
        bankid = found.id
    except bank.BANKS.DoesNotExist:
        found = None
        if found != None and found.id != None:
            flag = False
    return {"id": bankid, "name": name, "status": flag}


def get_customer_id(email):
    custid = -1
    name = ''
    flag = True
    try:
        found = customer.CUSTOMERS.objects.get(email=email)
        custid = found.id
        name = found.name
    except customer.CUSTOMERS.DoesNotExist:
        found = None
        if found != None and found.id != None:
            flag = False
    return {"id": custid, "name": name, "status": flag}
