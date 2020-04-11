from sqlalchemy import *

conStr="mysql+mysqlconnector://root:admin123@localhost:3306/testdb"
metadata=MetaData()
engine=create_engine(conStr)
conn=engine.connect().execution_options(schema_translate_map={None:"testdb"})
metadata = MetaData()

employees = Table('employees', metadata,
                  Column('employee_id', Integer, primary_key=True),
                  Column('employee_name', String(60), nullable=False),
                  # Column('employee_dept', Integer, ForeignKey("departments.department_id"))
                  )

# access the column "EMPLOYEE_ID":
employees.columns.employee_id
# or just
employees.c.employee_id
# via string
employees.c['employee_id']

# iterate through all columns
for c in employees.c:
    print(c)

# get the table's primary key columns
for primary_key in employees.primary_key:
    print(primary_key)

# get the table's foreign key objects:
for fkey in employees.foreign_keys:
    print(fkey)

# access the table's MetaData:
employees.metadata

# access the table's bound Engine or Connection, if its MetaData is bound:
employees.bind

# access a column's name, type, nullable, primary key, foreign key
employees.c.employee_id.name
employees.c.employee_id.type
employees.c.employee_id.nullable
employees.c.employee_id.primary_key
# employees.c.employee_dept.foreign_keys

# get the "key" of a column, which defaults to its name, but can
# be any user-defined string:
employees.c.employee_name.key

# access a column's table:
employees.c.employee_id.table is employees

# get the table related by a foreign key
# list(employees.c.employee_dept.foreign_keys)[0].column.table


conn.close()
engine=None


