import pyodbc

# # Connection example: Windows, without a DSN, using the Windows SQL Server driver
# cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;PORT=1433;DATABASE=testdb;UID=me;PWD=pass')

# Connection example: Linux, without a DSN, using the FreeTDS driver
# cnxn = pyodbc.connect('DRIVER={FreeTDS};SERVER=localhost;PORT=1433;DATABASE=testdb;UID=me;PWD=pass;TDS_Version=7.0')

# Connection example: with a DSN
conn = pyodbc.connect('DSN=dpTestDsn;PWD=')

cr = conn.cursor()
cr.execute("select * from table1")
row = cr.fetchall()
for rec in res:
    print(rec)


# cr.execute("insert into products(id, name) values (?, ?)", 'pyodbc', 'awesome library')
# conn.commit()


# cursor.execute(
#     """
#     delete
#       from products
#      where id <> 'pyodbc'
#     """)
