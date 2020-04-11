from collections import namedtuple

student=namedtuple('student','fname, lname, age')
students=[]
students.append(student('DP','clark',35))
students.append(student('DP1','clark2',25))
students.append(student('DP2','clar3',15))
students.append(student(fname='John', lname='Clarke', age='13'))

print("ordered dictionary from named tuple")
for s in students:
    print(s.fname,s.lname,s.age,s._asdict())

# s2 = s1._replace(age='14')
