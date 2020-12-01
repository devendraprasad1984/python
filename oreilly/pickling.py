from oreilly.first import getDatabase
import pickle
from pprint import pprint

# print(database)
database=getDatabase()
dbfile=open('peoples','wb')
pickle.dump(database,dbfile)
dbfile.close()
print('peoples saved')


readfile=open('peoples','rb')
dbs=pickle.load(readfile)
print('saved record look like as below')
pprint(dbs)
readfile.close()
