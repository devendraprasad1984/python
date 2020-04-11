"""
 Database management in PostgreSQL
 Psycopg2
pg8000
py-postgresql
PyGreSQL
sudo pip3 install psycopg2
login: sudo -u postgres psql
configure pwd: \password
CREATE DATABASE test;

"""
import psycopg2

def connect():
    try:
        conn = psycopg2.connect(database ="test",
                                user = "adith",
                                password = "password",
                                host = "localhost",
                                port = "5432")
        cur = conn.cursor()
    except (Exception, psycopg2.DatabaseError) as error:
        print ("Error while creating PostgreSQL table", error)
    return conn, cur

def create_table():
    conn, cur = connect()
    try:
        cur.execute('CREATE TABLE emp (id INT PRIMARY KEY, name VARCHAR(10),salary INT, dept INT)')
    except:
        print('error')
    conn.commit()

def insert_data(id = 1, name = '', salary = 1000, dept = 1):
    conn, cur = connect()
    try:
        cur.execute('INSERT INTO emp VALUES(%s, %s, %s, %s)',(id, name, salary, dept))
    except Exception as e:
        print('error', e)
    conn.commit()

def fetch_data():
    conn, cur = connect()
    try:
        cur.execute('SELECT * FROM emp')
    except:
        print('error !')
    data = cur.fetchall()
    return data

def print_data(data):
    print('Query result: ')
    print()
    for row in data:
        # printing the columns
        print('id: ', row[0])
        print('name: ', row[1])
        print('salary: ', row[2])
        print('dept: ', row[3])
        print('----------------------------------')

def delete_table():
    conn, cur = connect()
    try:
        cur.execute('DROP TABLE emp')
    except Exception as e:
        print('error', e)
    conn.commit()

if __name__ == '__main__':
    create_table()
    insert_data(1,"dp",1902)
    data=fetch_data()
    print_data(data)