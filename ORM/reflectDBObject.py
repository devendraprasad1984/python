from sqlalchemy import *
from sqlalchemy.engine import reflection
# The Inspector acts as a proxy to the reflection methods of the Dialect,

meta = MetaData()
conStr = "mysql+mysqlconnector://root:admin123@localhost:3306/testdb"
engine = create_engine(conStr)
dptest1 = Table('dptest1', meta, autoload=True, autoload_with=engine)
employessTable = Table('employees', meta, autoload=True, autoload_with=engine)
cols = [c.name for c in dptest1.columns]
print("named",cols,dptest1.columns['name'].name,dptest1.columns['age'])

for t in meta.tables:
    print("tables",t)

# access to all objects of the database such as tables views keys indexes etc
insp = reflection.Inspector.from_engine(engine)
allTables=insp.get_table_names()
print(allTables)
for t in allTables:
    tableFromDB= Table(t, meta, autoload=True, autoload_with=engine)
    cols = [c.name for c in tableFromDB.columns]
    print(t,"=>",cols)

dptest1= Table('dptest1', meta)
insp1 = reflection.Inspector.from_engine(engine)
insp1.reflecttable(dptest1, None)
print("object dptest1 inspected",dptest1.columns)

metaEmp=MetaData()
conStrEmpl = "mysql+mysqlconnector://root:admin123@localhost:3306/employees"
engineEmployees = create_engine(conStrEmpl)
employeeTable= Table('employees', metaEmp)
inspEmp = reflection.Inspector.from_engine(engineEmployees)
inspEmp.reflecttable(employeeTable, None)
print("object employees table inspected",employeeTable.columns)
selQuery=employeeTable.select(whereclause=employeeTable.columns['first_name']=='Georgi')
# selQuery=employeeTable.select()
res=engineEmployees.execute(selQuery)
print("via select clause of ORM")
for row in res:
    print(row)

print("via select query in clause")
res=engineEmployees.execute("select * from employees.employees where first_name like '%Georgi%' limit 2")
# print("found:",res.fetchall())
for row in res:
    print(row["emp_no"],row)


