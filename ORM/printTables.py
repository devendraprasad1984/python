from sqlalchemy import *
from sqlalchemy.sql import *
# from sqlalchemy import schema,String,INTEGER,sql

conStr="mysql+mysqlconnector://root:admin123@localhost:3306/testdb"

metadata=MetaData()
dptest1_table=Table(
    'dptest1',metadata,
    Column('name',String(100)),
    Column('age',INTEGER)
)
print("loop over tables in metadata object")
for t in metadata.sorted_tables:
    print(t.name)

engine=create_engine(conStr)
conn=engine.connect().execution_options(schema_translate_map={None:"testdb"})
print("print from engine connected to db")
for t in engine.table_names():
    print("...",t)

sqQuery=select([dptest1_table]).where(dptest1_table.columns["name"].endswith('dev', escape="^", autoescape=True))
print(sqQuery)

# stmt.where(
#     column.in_(
#         select([othertable.c.y]).
#             where(table.c.x == othertable.c.x)
#     )
# )
conn=None
engine=None



