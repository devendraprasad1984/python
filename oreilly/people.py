from oreilly.person import Person, Manager
import shelve

bob=Person('Bob Smith',20,4000)
sue=Person('Sue Johnson',50,6000)
tom=Manager('tom harrington',35,8900)
people=[bob, sue, tom]
for p in people: p.giveRaise(10) #every employee 10% but manager 20% due to class of manager implementation, polymorphysm
#what happens is because of object is processed depends on which class
namePay=[(p.name, p.job, p.pay) for p in people]
print(namePay)
#make object persistent to disk
db = shelve.open('class-people-shelve')
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom
db.close()

