from django.shortcuts import render, HttpResponse as res
from django.views.decorators.csrf import csrf_exempt
from loan_manager.common import config, utils
import json
from . import models


@csrf_exempt
def fn_LOAN(req):
    if req.method == 'GET':
        return res(config.NO_OP_ALLOWED)
    body = config.getBodyFromReq(req)
    bank_name = body['bank_name']
    email = body['email']
    loan_amount = body['loan_amount']
    rate = body['rate']
    period = body['year']

    bank = utils.check_bank_exists(bank_name)
    customer = utils.check_customer_exists(email)
    bankid = bank["id"]
    bankFoundObject = bank['object']

    customerid = customer["id"]
    customername = customer["name"]
    loan_limit = customer["loan_limit"]
    customerFoundObject = customer['object']
    customerLoanCalc = customer['loan_calc']
    total_number_of_loans = customerLoanCalc['count']
    total_loaned_value = customerLoanCalc['total_loan_amount']
    credit_loan_left = float(loan_limit) - total_loaned_value
    cannot_sanction_loan = credit_loan_left < loan_amount
    if cannot_sanction_loan == True:
        output = {
            "msg": f"cannot sanction loan to customer {customername}, {email} due to his credit rating",
            "status": False
        }
        return res(json.dumps(output), content_type=config.CONTENT_TYPE)

    interest_amount = round(loan_amount * (rate / 100) * period, 2)
    emi_months = period * 12  # number of emis
    total_amount_pi = round(loan_amount + interest_amount, 2)
    emi_amount = round(total_amount_pi / emi_months, 2)
    try:
        uid = config.get_uniq_loanid()
        model = models.LOANS(
            uid=uid,
            bankid=bankFoundObject,
            customerid=customerFoundObject,
            loan_amount=loan_amount,
            rate=rate,
            period=period,
            interest_amount=interest_amount,
            emi_months=emi_months,
            emi_amount=emi_amount,
            total_amount_pi=total_amount_pi
        )
        model.save()
        config.addlog(f'loan added for customer {customerid} - {customername} from bank {bankid} - {bank_name}', body)
        success = {
            "msg": f'CREDIT LOAN LEFT LIMIT {credit_loan_left}. This customer already has {total_number_of_loans} running worth {total_loaned_value}. '
                   f'loan for Mr/Mrs {customername}(customer id: {customerid}, email: {email}) from bank {bank_name}({bankid}) has been granted. '
                   f'Your remaining loan limit as per your credit score is {loan_limit:,}. '
                   f'Your unique loan reference is {uid}. you have taken a loan of amount {loan_amount:,} for a period of {period} yrs @rate {rate}% '
                   f'per annum and you have to pay an emi of amount {emi_amount:,} per month for next {emi_months} months. You will be paying P+I={total_amount_pi:,}, '
                   f'total interest paid by you will be {interest_amount:,}. Your auto debit will start next month.',
            "status": config.success
        }
        flag = True
    except Exception as ex:
        config.adderror('loan error', str(ex))
        failed = {
            "msg": f'loan for {bank_name} could not be added',
            "detail": str(ex),
            "status": config.failed
        }
        flag = False
    # failed = {
    #     "msg": f'{"failed"}',
    #     "status": config.failed
    # }
    output = success if flag == True else failed
    return res(json.dumps(output), content_type=config.CONTENT_TYPE)


@csrf_exempt
def fn_PAYMENT(req):
    return res('PAYMENT')


@csrf_exempt
def fn_BALANCE(req):
    return res('BALANCE')
