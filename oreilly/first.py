
def getDatabase():
    database={}
    bob = {'name': 'Bob Smith', 'age': 42, 'pay': 30000, 'job': 'dev'}
    sue = {'name': 'Sue Jones', 'age': 45, 'pay': 40000, 'job': 'hdw'}
    database['bob']=bob
    database['sue']=sue
    database['tom'] = dict(name='Tom', age=50, job=None, pay=0)
    return database

def callMain():
    database={}
    people = [['devendra prasad', 4000, 'software'], ['ravi kumar', 6000, 'hardware'], ['raj kumar', 8000, 'nicer']]

    NAME, PAY, Prof = range(3); #field labels
    for p in people:
        p[1] *= 1.25
        print('printing by labels', NAME, PAY, Prof, p[NAME], p[PAY], p[Prof]);

    # using list generator
    allPays = [p[1] for p in people]
    print('all pays', allPays)

    # using map as its a generator
    allPays = map(lambda x: x[1], people)
    payList = list(allPays);
    print('all pays', payList, '#generator expression', sum(payList))

    def field(record, label):
        for (name, value) in record:
            if name==label: return value

    bob = [['name', 'Bob Smith'], ['age', 42], ['pay', 10000]]
    sue = [['name', 'Sue Jones'], ['age', 45], ['pay', 20000]]
    people=[bob, sue]
    # for p in people:
    #     for (k,v) in p:
    #         # print(p, k,v)
    #         # if k=='name': print(v)
    #         print(field(p,'name'))
    #         print(field(p,'pay'))
    print('bobs pay is',field(bob,'pay'))
    print('sues age is',field(sue,'age'))


    # more efficient objects are dictionaries for key=>value associations
    bob = {'name': 'Bob Smith', 'age': 42, 'pay': 30000, 'job': 'dev'}
    sue = {'name': 'Sue Jones', 'age': 45, 'pay': 40000, 'job': 'hdw'}
    database['bob']=bob
    database['sue']=sue

    people=[bob, sue]
    print('objects',bob,sue)
    print('objects-NAME',bob['name'],bob['age'])
    print('objects-NAME',sue['name'],sue['age'])

    names = ['name', 'age', 'pay', 'job']
    values = ['Sue Jones', 45, 40000, 'hdw']
    print(list(zip(names, values)))
    print(dict(zip(names, values)))


    names=[p['name'] for p in people if p['age']<45] #sql-ish query
    print('names of all people', names)


    bob2 = {'name': {'first': 'Bob', 'last': 'Smith'}, 'age': 42,
            'job': ['software', 'writing'], 'pay': (40000, 50000)}
    print('bob2 nested structure', bob2['name'], bob2['pay'])

    # dictionary of dictionaries
    from pprint import pprint
    print('dict of dict object')
    pprint(database)
    for key in database:
        print(key, '=>',database[key]['name'],': ',database[key]['pay'])
    for key in database.keys():
        print(key, '=>',database[key]['name'],': ',database[key]['pay'])
    for (key,values) in database.items():
        print(key, values)
    for obj in database.values():
        print(obj,obj['name'],obj['pay'])
    x = [database[key]['name'] for key in database]
    y = [rec['pay'] for rec in database.values()]
    pprint(x)
    pprint(y)

    database['tom'] = dict(name='Tom', age=50, job=None, pay=0)
    print(database.keys())
    # dict of dict is how objects are stored permanently in database
    # the pythonic technique is called shelve

if __name__=='__main__':
    callMain()
