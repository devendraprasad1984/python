import pymysql.cursors

# Connect to the database
connection = pymysql.connect(
    host='localhost',
    db='dptests',
    user='root',
    password='admin1234',
)

try:
    # with connection.cursor() as cursor:
    #     # Create a new record
    #     sql = "INSERT INTO table1(name,age,subject,marks) VALUES (%s,%s,%s,%s)"
    #     cursor.execute(sql, ('dp', '34', 'Maths', '97'))
    #     connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT name,age,subject,marks FROM table1"
        cursor.execute(sql)
        result = cursor.fetchall()
        # print(result)
        print('name','age','subject','marks')
        for x in result:
            y=[z for z in x] #convert tuple into list for modifiction is any
            print(y)
            print(x[0],x[1],x[2],x[3])
finally:
    connection.close()
