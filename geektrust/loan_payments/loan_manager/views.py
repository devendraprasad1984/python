from django.shortcuts import render, HttpResponse as res
from django.views.decorators.csrf import csrf_exempt
from loan_manager.common import config, utils
import json


@csrf_exempt
def fn_LOAN(req):
    if req.method == 'GET':
        return res(config.NO_OP_ALLOWED)
    body = config.getBodyFromReq(req)
    uid = config.get_uniq_loanid()
    bank_name = body['bank_name']
    email = body['email']
    bank = utils.get_bank_id(bank_name)
    customer = utils.get_customer_id(email)
    bankid = bank["id"]
    customerid = customer["id"]
    customername = customer["name"]
    loan_amount = 0
    rate = 0
    period = 1
    interest_amount = round(loan_amount * (rate / 100) * period, 2)
    emi_months = period * 12 * period #number of emis
    repaid_amount = 0
    total_amount_PI = loan_amount + interest_amount
    emi_amount = 0
    inputs = {"loan_amount": loan_amount, "rate": rate, "period": period, "repaid_amount": repaid_amount}
    flag = True
    success = {
        "msg": f'loan for Mr/Mrs {customername}(customer id: {customerid}, email: {email}) from bank {bank_name}({bankid}) has been granted - {uid}',
        "status": config.success
    }
    failed = {
        "msg": f'{"failed"}',
        "status": config.failed
    }
    output = success if flag == True else failed
    return res(json.dumps(output), content_type=config.CONTENT_TYPE)


@csrf_exempt
def fn_PAYMENT(req):
    return res('PAYMENT')


@csrf_exempt
def fn_BALANCE(req):
    return res('BALANCE')
