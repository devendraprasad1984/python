import copy
import json

from bank_manager import models as bank
from customer_manager import models as customer
from loan_manager import models as loan_model
from subscribe import models as subscriber
from . import utils, field_names


def check_field_existence_in_request_body(body, fld_names):
    presence_flag = True
    msg = copy.deepcopy(utils.MISSING_FIELD_MSG)
    flds_in_body = ', '.join(body) + ' | ' + body.__len__().__str__()
    flds_expected = ', '.join(fld_names) + ' | ' + fld_names.__len__().__str__()
    msg[field_names.expected] = flds_expected
    msg[field_names.given] = flds_in_body
    for f in fld_names:
        if f not in body or body[f] == '' or body[f] == None:
            presence_flag = False
            break
    return presence_flag, json.dumps(msg)

def check_bank_exists(name, uid, id):
    id = -1
    flag = True
    try:
        if name != None:
            found = bank.BANKS.objects.get(name=name)
        elif uid != None:
            found = bank.BANKS.objects.get(uid=uid)
        elif id != None:
            found = bank.BANKS.objects.get(id=id)

        id = found.id
    except bank.BANKS.DoesNotExist:
        found = None
        if found != None and found.id != None:
            flag = False
    return {"id": id, "name": name, "status": flag, "object": found}

def check_customer_all_loan(customer_id):
    id = -1
    flag = True
    try:
        found = loan_model.LOANS.objects.filter(customerid=customer_id)
        total_loan_amount = utils.getSum(found, 'loan_amount')
        total_repaid_amount = utils.getSum(found, 'repaid_amount')
        total_interest_amount = utils.getSum(found, 'interest_amount')
    except loan_model.LOANS.DoesNotExist:
        found = None
        if found != None and found.id != None:
            flag = False
    return {
        "customerid": customer_id,
        "total_loan_amount": total_loan_amount,
        "total_repaid_amount": total_repaid_amount,
        "total_interest_amount": total_interest_amount,
        "status": flag,
        "object": found,
        "count": len(found) if found != None else 0
    }

def check_customer_exists(email, uid, id):
    id = -1
    name = ''
    loan_limit = 0
    found_loan = None
    found = None
    flag = True
    try:
        if email != None:
            found = customer.CUSTOMERS.objects.get(email=email)
        elif uid != None:
            found = customer.CUSTOMERS.objects.get(uid=uid)
        elif id != None:
            found = customer.CUSTOMERS.objects.get(id=id)
        id = found.id
        name = found.name
        loan_limit = found.loan_limit
        found_loan = check_customer_all_loan(id)
    except customer.CUSTOMERS.DoesNotExist:
        if found != None and found.id != None:
            flag = False
    return {"id": id, "name": name, "loan_limit": loan_limit, "loan_calc": found_loan, "status": flag, "object": found}

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
    return {"id": id, "name": name, "status": flag, "object": found}

def check_customer_or_bank_or_loan(id):
    if id == -1: return False
    return True

def get_existing_loan_details(bankid=None, customerid=None, loan_ref=None):
    id = -1
    uid = ''
    flag = True
    try:
        if loan_ref != None and bankid == None and customerid == None:
            found = loan_model.LOANS.objects.filter(uid=loan_ref)
            found_list = utils.getList(found)[0]
            id = found_list['id']
        elif loan_ref != None and bankid != None and customerid != None:
            found = loan_model.LOANS.objects.filter(bankid=bankid, customerid=customerid, uid=loan_ref)
            found_list = utils.getList(found)[0]
            id = found_list['id']
            uid = found_list['uid']
        elif bankid == None and customerid == None:
            found = loan_model.LOANS.objects.filter(bankid=bankid, customerid=customerid)
            found_list = utils.getJsonSet(found)
    except loan_model.LOANS.DoesNotExist:
        found = None
        if found != None and found.id != None:
            flag = False
    return {"id": id, "uid": uid, "status": flag, "object": found_list}
