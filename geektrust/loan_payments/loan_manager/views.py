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
    loan_amount = body['loan_amount']
    rate = body['rate']
    period = body['year']

    bank = utils.get_bank_id(bank_name)
    customer = utils.get_customer_id(email)
    bankid = bank["id"]
    customerid = customer["id"]
    customername = customer["name"]
    loan_limit = customer["loan_limit"]

    interest_amount = round(loan_amount * (rate / 100) * period, 2)
    emi_months = period * 12 #number of emis
    repaid_amount = 0
    total_amount_PI = loan_amount + interest_amount
    emi_amount = total_amount_PI / emi_months
    inputs = {"loan_amount": loan_amount, "rate": rate, "period": period, "repaid_amount": repaid_amount}
    flag = True
    success = {
        "msg": f'loan for Mr/Mrs {customername}(customer id: {customerid}, email: {email}) from bank {bank_name}({bankid}) has been granted. '
               f'Your remaining loan limit as per your credit score is {loan_limit:,}. '
               f'Your unique loan reference is {uid}. you have taken a loan of amount {loan_amount:,} for a period of {period} yrs @rate {rate}% '
               f'per annum and you have to pay an emi of amount {emi_amount:,} per month for next {emi_months} months. You will be paying P+I={total_amount_PI:,}, '
               f'total interest paid by you will be {interest_amount:,}. Your auto debit will start next month.',
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
