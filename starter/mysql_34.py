import pymysql.cursors


def openConn():
    try:
        conn = pymysql.connect(user='root', password='', host='localhost', database='test',
                               cursorclass=pymysql.cursors.DictCursor)
        print("Connection Opened Successfully")
        return conn
    except Exception as ex:
        print(ex)


def closeConn(conn):
    conn.close()
    print("closed connection")


def getData(conn):
    with conn.cursor() as cr:
        sql = "select * from table1"
        # gives data back in json format
        cr.execute(sql)
        # res=cr.fetchone()
        res = cr.fetchall()
        # print(res)
        for rec in res:
            print(rec)
        # print(rec["name"]+"|"+str(rec["age"])+"|"+rec["city"])


def insertData(conn):
    with conn.cursor() as cr:
        # vals=("testData","28","M","New Delhi",)
        # sql="insert into table1(name,age,gender,city) values(?,?,?,?);"
        sql = "insert into table1(name,age,gender,city) values('test',54,'M','Chennai');"
        cr.execute(sql)
        # cr.execute(sql,vals)
        print("INSERTED: " + sql)
    conn.commit()


conn = openConn()
getData(conn)
# insertData(conn)
closeConn(conn)
