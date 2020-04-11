import cx_Oracle

# http://www.oracle.com/technetwork/articles/dsl/python-091105.html
con = cx_Oracle.connect('pythonhol/welcome@127.0.0.1/orcl')
print
con.version
con.close()
