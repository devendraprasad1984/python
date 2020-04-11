from sets import Set

engineers = Set(['John', 'Jane', 'Jack', 'Janice'])
programmers = Set(['Jack', 'Sam', 'Susan', 'Janice'])
managers = Set(['Jane', 'Jack', 'Susan', 'Zack'])
employees = engineers | programmers | managers  # union
engineering_management = engineers & managers  # intersection
fulltime_management = managers - engineers - programmers  # difference
engineers.add('Marvin')  # add element
print(engineers)

Set(['Jane', 'Marvin', 'Janice', 'John', 'Jack'])
check1 = employees.issuperset(engineers)
print("is engineer a superset in employee: " + str(check1))  # superset test
employees.update(engineers)  # update from another set
check2 = employees.issuperset(engineers)
print("is engineer a superset in employee: " + str(check2))

for group in [engineers, programmers, managers, employees]:
    group.discard('Susan')  # unconditionally remove element
    print(group)
