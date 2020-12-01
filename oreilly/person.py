class Person:
    def __init__(self,name,age,pay=0,job='Employee'):
        self.name=name
        self.age=age
        self.pay=pay
        self.job=job
    def getLastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        changedBy=(1 + percent / 100)
        self.pay *= changedBy
    def __str__(self):
        #operator overloading
        print(self.__dict__)
        return '<%s => %s>' % (self.__class__.__name__, self.name)


class Manager(Person):
    def __init__(self,name,age,pay):
        Person.__init__(self,name,age,pay,'Manager')
    #polymorphysm
    def giveRaise(self, percent, bonus=10):
        # self.pay*=(1+percent/100+bonus)
        Person.giveRaise(self, percent+bonus)


if __name__=='__main__':
    bob=Person('Bob Smith',20,50000,'software')
    sue=Person('Sue Johnson',30,40000,'hardware')
    print(bob)
    print(bob.name,sue.name,bob.pay,sue.pay)
