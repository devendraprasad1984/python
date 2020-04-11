from sqlalchemy import *
# from sqlalchemy import schema,String,INTEGER,sql

conStr="mysql+mysqlconnector://root:admin123@localhost:3306/testdb"

metadata=MetaData()
dptest1_table=Table(
    'dptest1',metadata,
    Column('name',String(100)),
    Column('age',INTEGER)
)
print("cols",dptest1_table.columns)

engine=create_engine(conStr)
conn=engine.connect().execution_options(schema_translate_map={None:"testdb"})


# runs a transaction
trans=conn.begin()
r1 = conn.execute("insert into dptest1 values('kumar',40)" ) #autocommit
print("res back",r1)
trans.commit()

print("from select query")
rs=conn.execute("select * from dptest1")
for r in rs:
    print(r,r["name"],r["age"])
rs.close()

print("from ORM concept")
rs=conn.execute(dptest1_table.select())
for r in rs:
    print(r,r["name"],r["age"])
rs.close()



print("from inline from sql")
for r in engine.execute("select * from dptest1"):
    print(r,r["name"],r["age"])


conn.close()
engine=None



