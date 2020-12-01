from oreilly.first import getDatabase
import shelve
from pprint import pprint

# write into shelved object
database=getDatabase()
db=shelve.open('shelvedPeople')
db['bob']=database['bob']
db['sue']=database['sue']
db['tom']=database['tom']
db.close()

# read from shelved object
db=shelve.open('shelvedPeople')
db['harry'] = dict(name='Harry', age=36, job=None, pay=0)
pprint([db[key] for key in db])
db.close()

