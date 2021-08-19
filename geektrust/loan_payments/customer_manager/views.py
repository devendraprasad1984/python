from django.shortcuts import render, HttpResponse as res
from django.views.decorators.csrf import csrf_exempt
from loan_manager.common import utils, queries
from customer_manager import models
import json
from .validations import validate as customerValidations


# Create your views here.
@csrf_exempt
def fn_ADD_CUSTOMER(req):
    if req.method == 'GET':
        return res(utils.NO_OP_ALLOWED)

    body = utils.getBodyFromReq(req)
    name = body['name']
    age = body['age']
    email = body['email']
    loan_limit = body['loan_limit']
    inputs = {"name": name, "email": email, "age": age, "limit": loan_limit}
    flag = True
    validate = customerValidations.validate_input_add_new_customer(inputs)
    if validate['status'] == True:
        try:
            uid = utils.get_uniq_customerid()
            model = models.CUSTOMERS(
                name=name,
                uid=uid,
                age=age,
                email=email,
                loan_limit=loan_limit
            )
            model.save()
            utils.addlog('customer', body)
            success = {
                "msg": f'customer {name}, {email}, {age} yrs, having loan {loan_limit} added - {uid}',
                "status": utils.success
            }
        except Exception as ex:
            failed = {
                "msg": f'customer {name} {email} not added',
                "detail": str(ex),
                "status": utils.failed
            }
            flag = False
            utils.adderror('customer error', str(ex))
    else:
        flag = False
        failed = {
            "msg": f'{validate["msg"]}',
            "status": utils.failed
        }

    output = success if flag == True else failed
    return res(json.dumps(output), content_type=utils.CONTENT_TYPE)


@csrf_exempt
def fn_GET_LIST_of_CUSTOMERS(req):
    if req.method == utils.POST:
        return res(utils.NO_OP_ALLOWED)
    # model=models.CUSTOMERS.objects.only('id', 'name', 'uid', 'age', 'loan_limit', 'when').order_by('id')
    # datasetObj=models.CUSTOMERS.objects.raw(queries.CUSTOMERSWITHLOANS)
    dataset = queries.CUSTOM_QUERY_RUN(queries.getCustomerWithLoanQuery())
    # model1=loanModel.objects.select_related('bankid', 'customerid')
    # data = config.getJsonSet(model1)
    output = {"data": dataset['json']}
    # print('list of customers with loans', output)
    utils.addlog('customer', {'customer_fetch': True})
    return res(json.dumps(output), content_type=utils.CONTENT_TYPE)
