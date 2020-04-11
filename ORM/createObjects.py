from sqlalchemy import *

conStr="mysql+mysqlconnector://root:admin123@localhost:3306/testdb"
metadata=MetaData()
engine=create_engine(conStr)
conn=engine.connect().execution_options(schema_translate_map={None:"testdb"})
print("creating objects using metadata")
metadata = MetaData()
user = Table('user', metadata,
             Column('user_id', Integer, primary_key=True),
             Column('user_name', String(16), nullable=False),
             Column('email_address', String(60), key='email'),
             Column('nickname', String(50), nullable=False)
             )
user_prefs = Table('user_prefs', metadata,
                   Column('pref_id', Integer, primary_key=True),
                   Column('user_id', Integer, ForeignKey("user.user_id"), nullable=False),
                   Column('pref_name', String(40), nullable=False),
                   Column('pref_value', String(100))
                   )

employees = Table('employees', metadata,
                  Column('employee_id', Integer, primary_key=True),
                  Column('employee_name', String(60), nullable=False),
                  # Column('employee_dept', Integer, ForeignKey("departments.department_id"))
                  )
metadata.create_all(engine)
conn.close()
engine=None



