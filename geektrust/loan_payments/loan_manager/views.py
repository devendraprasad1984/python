from django.shortcuts import render, HttpResponse as res
from django.views.decorators.csrf import csrf_exempt
from loan_manager.common import utils, lookup, field_names
import json
from . import models

msg_entity_doesnt_exist = {
    "msg": f'bank | customer | loan or all association doesnt exist',
    "status": False
}


@csrf_exempt
def fn_LOAN(req):
    if req.method == 'GET':
        return res(utils.NO_OP_ALLOWED)
    body = utils.getBodyFromReq(req)
    bank_name = body[field_names.bank_name]
    email = body[field_names.email]
    loan_amount = body[field_names.loan_amount]
    rate = body[field_names.rate]
    period = body[field_names.year]

    bank = lookup.check_bank_exists(bank_name)
    customer = lookup.check_customer_exists(email)
    bankid = bank[field_names.id]
    customerid = customer[field_names.id]
    bank_entity_exist_check = lookup.check_customer_or_bank_or_loan(bankid)
    customer_entity_exist_check = lookup.check_customer_or_bank_or_loan(customerid)
    if bank_entity_exist_check == False or customer_entity_exist_check == False:
        return res(json.dumps(msg_entity_doesnt_exist), content_type=utils.CONTENT_TYPE)

    bankFoundObject = bank[field_names.object]
    customername = customer[field_names.name]
    loan_limit = customer[field_names.loan_limit]
    customerFoundObject = customer[field_names.object]
    customerLoanCalc = customer[field_names.loan_calc]
    total_number_of_loans = customerLoanCalc[field_names.count]
    total_loaned_value = customerLoanCalc[field_names.total_loan_amount]
    credit_loan_left = float(loan_limit) - total_loaned_value
    cannot_sanction_loan = credit_loan_left < loan_amount
    if cannot_sanction_loan == True:
        output = {
            "msg": f"cannot sanction loan to customer {customername}, {email} due to his credit rating",
            "status": False
        }
        return res(json.dumps(output), content_type=utils.CONTENT_TYPE)

    interest_amount = round(loan_amount * (rate / 100) * period, 2)
    emi_months = period * 12  # number of emis
    total_amount_pi = round(loan_amount + interest_amount, 2)
    emi_amount = round(total_amount_pi / emi_months, 2)
    try:
        uid = utils.get_uniq_loanid()
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
        utils.addlog(f'loan added for customer {customerid} - {customername} from bank {bankid} - {bank_name}', body)
        success = {
            "msg": f'CREDIT LOAN LEFT LIMIT {credit_loan_left}. This customer already has {total_number_of_loans} running worth {total_loaned_value}. '
                   f'loan for Mr/Mrs {customername}(customer id: {customerid}, email: {email}) from bank {bank_name}({bankid}) has been granted. '
                   f'Your remaining loan limit as per your credit score is {loan_limit:,}. '
                   f'Your unique loan reference is {uid}. you have taken a loan of amount {loan_amount:,} for a period of {period} yrs @rate {rate}% '
                   f'per annum and you have to pay an emi of amount {emi_amount:,} per month for next {emi_months} months. You will be paying P+I={total_amount_pi:,}, '
                   f'total interest paid by you will be {interest_amount:,}. Your auto debit will start next month.',
            "status": utils.success
        }
        status_flag = True
    except Exception as ex:
        utils.adderror('loan error', str(ex))
        failed = {
            "msg": f'loan for {bank_name} could not be added',
            "detail": str(ex),
            "status": utils.failed
        }
        status_flag = False
    output = success if status_flag == True else failed
    return res(json.dumps(output), content_type=utils.CONTENT_TYPE)


@csrf_exempt
def fn_PAYMENT(req):
    return res('PAYMENT')


@csrf_exempt
def fn_BALANCE(req):
    if req.method == 'GET':
        return res(utils.NO_OP_ALLOWED)

    body = utils.getBodyFromReq(req)
    bank_name = body[field_names.bank_name]
    email = body[field_names.email]
    loan_ref = body[field_names.loan_ref]
    emi_number = body[field_names.emi_number]

    bank = lookup.check_bank_exists(bank_name)
    customer = lookup.check_customer_exists(email)
    bankid = bank[field_names.id]
    customerid = customer[field_names.id]
    loan_details_customer = lookup.get_existing_loan_by_bank_customer_id(bankid, customerid, loan_ref)
    loan_id = loan_details_customer[field_names.id]
    loan_uid = loan_details_customer[field_names.uid]
    loan_object = loan_details_customer[field_names.object]
    if loan_id != -1:
        emi_amount = loan_object[field_names.emi_amount]
        emi_months = loan_object[field_names.emi_months]
        emi_months_repaid = loan_object[field_names.emi_months_repaid]
        repaid_amount = loan_object[field_names.repaid_amount]
        loan_amount = loan_object[field_names.loan_amount]

    bank_entity_exist_check = lookup.check_customer_or_bank_or_loan(bankid)
    customer_entity_exist_check = lookup.check_customer_or_bank_or_loan(customerid)
    loan_entity_exist_check = lookup.check_customer_or_bank_or_loan(loan_id)
    if bank_entity_exist_check == False or customer_entity_exist_check == False or loan_entity_exist_check == False:
        return res(json.dumps(msg_entity_doesnt_exist), content_type=utils.CONTENT_TYPE)

    customer_name = customer[field_names.name]

    msg = {
        "msg": f'Balances= {bank_name}({bankid}) - customer: {customer_name}, email: {email}, emi: {emi_number}, loan: {loan_uid}({loan_id})'
               f'loan amount: {loan_amount}, emi amount: {emi_amount}, emi months: {emi_months}, emi repaid: {repaid_amount}, emi_months_repaid:{emi_months_repaid}',
        "loan_details": utils.jsonEncode(loan_object),
        "status": True
    }
    utils.addlog(f'balance check {customer_name}({customerid}) / {bank_name}({bankid})', body)
    return res(json.dumps(msg), content_type=utils.CONTENT_TYPE)
