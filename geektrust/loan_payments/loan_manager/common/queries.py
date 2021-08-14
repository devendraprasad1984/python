from django.db import connection
from . import config

CUSTOMERSWITHLOANS = f'select * from customer_manager_customers a left outer join loan_manager_loans b ON ' \
                     f'a.id=b.customerid_id order by a.id'


def CUSTOM_QUERY_RUN(qur):
    cursor = connection.cursor()
    getfield = lambda i: cursor.description[i][0]
    cursor.execute(qur)
    rows = cursor.fetchall()
    jsondata = [dict((getfield(i), value) for i, value in enumerate(row)) for row in rows]
    cursor.connection.close()
    return {"rows": rows, "json": config.jsonEncode(jsondata)}
