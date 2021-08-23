from django.db import connection

from . import utils


def getCustomerWithLoanQuery(**param):
    id = param['id']
    loan_ref = param['loan_ref']
    qur = f'select a.id as customerid,b.bankid_id as bankid, a.email,a.name,a.loan_limit,a.uid as cust_uid,b.uid as loan_uid, b.rate,b.period,b.loan_amount '
    qur += f',b.interest_amount,b.emi_months,b.emi_months_repaid,b.repaid_amount,b.emi_amount,b.total_amount_pi,b.when'
    qur += f' from customer_manager_customers a left outer join loan_manager_loans b ON '
    qur += f' a.id=b.customerid_id'
    qur += (f' where a.id={id} and b.bankid_id is not null' if id != None else '')
    qur += (f' where b.uid={loan_ref}' if loan_ref != None else '')
    qur += f' order by a.id'
    return qur

def CUSTOM_QUERY_RUN(qur):
    cursor = connection.cursor()
    getfield = lambda i: cursor.description[i][0]
    cursor.execute(qur)
    rows = cursor.fetchall()
    jsondata = [dict((getfield(i), value) for i, value in enumerate(row)) for row in rows]
    cursor.connection.close()
    return {"rows": rows, "json": utils.jsonEncode(jsondata)}
