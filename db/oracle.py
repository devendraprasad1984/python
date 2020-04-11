import cx_Oracle


# http://www.oracle.com/technetwork/articles/dsl/python-091105.html
# db1 = cx_Oracle.connect('hr/hrpwd@localhost:1521/XE')
# dsn_tns = cx_Oracle.makedsn('localhost', 1521, 'XE')
# db2 = cx_Oracle.connect('hr', 'hrpwd', dsn_tns)

def conn():
    con = cx_Oracle.connect('system/newuser123#@127.0.0.1/XE')
    print("connected to database: " + con.version)
    return con


# con.close()

def getTable(con):
    cursor = con.cursor()
    cursor.execute('select * from XE.table1')
    colnames = [i[0] for i in cursor.description]  # column names
    # fields = [i[1] for i in cursor.description] # field types
    # print(colnames)
    # print(fields)
    result = [dict(zip(colnames, row)) for row in cursor]  # list comprehension to wrap db call into dictiory object
    # print(result)
    # for row in cursor:
    # 	# print (row)
    # 	print(str(row[0])+"|"+row[1]+"|"+row[2]+"|"+row[3])
    # 	# row[3]="test" #this is immutable, hence cannot be changed here

    # res = cursor.fetchall()
    # print (res)
    cursor.close()

    # iterate over dictionary any number of times
    for ir in result: print(ir)


# cur.prepare('select * from departments where department_id = :id')
# r1 = cursor.execute('SELECT * FROM locations WHERE country_id=:1 AND city=:2', ('US', 'Seattle'))

# cur.execute(None, {'id': 210})
# res = cur.fetchall()
# print res

# cur.execute(None, {'id': 110})
# res = cur.fetchall()
# print res


# few alternate ways
# res = cur.fetchall()
# for r in res:

# wrap row into dictionary via generator expression
# def rows_as_dicts(cursor):
#     """ returns cx_Oracle rows as dicts """
#     colnames = [i[0] for i in cursor.description]
#     for row in cursor:
#         yield dict(zip(colnames, row))



# calling conn
con = conn()
print("conn object: " + str(con))
getTable(con)
con.close()

# destruct the object
del con
print("connection object cleaned up")
