from bank_manager import models as bank
from customer_manager import models as customer
from loan_manager import models as loan_model
from subscribe import models as subscriber
from . import config


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
    return {"id": id, "name": name, "status": flag, "object": found}


def check_customer_loan(customer_id):
    id = -1
    flag = True
    try:
        found = loan_model.LOANS.objects.filter(customerid=customer_id)
        total_loan_amount = config.getSum(found, 'loan_amount')
        total_repaid_amount = config.getSum(found, 'repaid_amount')
        total_interest_amount = config.getSum(found, 'interest_amount')
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
        "object": found
    }


def check_customer_exists(email):
    id = -1
    name = ''
    flag = True
    try:
        found = customer.CUSTOMERS.objects.get(email=email)
        id = found.id
        name = found.name
        loan_limit = found.loan_limit
        found_loan = check_customer_loan(id)
    except customer.CUSTOMERS.DoesNotExist:
        found = None
        if found != None and found.id != None:
            flag = False
    return {"id": id, "name": name, "loan_limit": loan_limit,"loan_calc":found_loan, "status": flag, "object": found}


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
