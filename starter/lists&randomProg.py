# list comprehension - create lists in very east and natureal way
# The following are common ways to describe lists (or sets, or tuples, or vectors) in mathematics.
# S = {x² : x in {0 ... 9}}
# V = (1, 2, 4, 8, ..., 2¹²)
# M = {x | x in S and x even}
# http://www.secnetix.de/olli/Python/list_comprehensions.hawk

S = [x ** 2 for x in range(10)]  # power of 2 until 10
V = [2 ** i for i in range(13)]  # powe of i over 2 until 13, basically 2 raise to powe 13 in end
M = [x for x in S if x % 2 == 0]

print(S)
print(V)
print(M)

# List comprehensions are a tool for transforming one list (any iterable actually) into another list.
# During this transformation, elements can be conditionally included in the new list and each element can be transformed as needed.


noprimes = [j for i in range(2, 8) for j in range(i * 2, 50, i)]
primes = [x for x in range(2, 50) if x not in noprimes]
print(primes)
print(noprimes)

words = 'The quick brown fox jumps over the lazy dog'.split()
print(words)
stuff = [[w.upper(), w.lower(), len(w)] for w in words]

for element in stuff:
    print(element)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
doubleIt = [x * 2 for x in numbers if x % 2 == 1]

x = 1
y = 1
z = 1
n = 2
lst = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if (i + j + k) != n]
print("tripplet list comprehension", lst)

print("find second highest values or runner up score")
arr = [2, 3, 6, 6, 5]
narr = []
for x in arr:
    if not narr.__contains__(x):
        narr.append(x)
narr.sort(key=lambda x: x, reverse=True)
print(narr, narr[1])

print("second lowest grades")
students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
students=['Harsh',20],['Beria',20],['Varun',19],['Kakunami',19],['Vikas',21]
students = [['Rachel', -50],['Mawer',-50],['Sheen', -50],['Shaheen', 51]]
students=['Sona',-25.001],['Mona',-25.0001],['Mini',-25.000],['Rita',-25.0]

sgrades = []
lowest_grade_holders = []
for s in students:
    if not sgrades.__contains__(s[1]):
        sgrades.append(s[1])
sgrades.sort()
print(sgrades)
second_lowest=0
if sgrades.__len__()<=1:
    second_lowest=sgrades[0]
else:
    second_lowest = sgrades[1]
# print("smallest number in list", min(sgrades), sgrades[1])
for x in students:
    if second_lowest == x[1]:
        lowest_grade_holders.append(x[0])
lowest_grade_holders.sort()
for x in lowest_grade_holders:
    print(x)

"""
You have a record of  students. Each record contains the student's name, and their percent marks in Maths, Physics and Chemistry. The marks can be floating values. The user enters some integer  followed by the names and marks for students. You are required to save the record in a dictionary data type. The user then enters a student's name. Output the average percentage marks obtained by that student, correct to two decimal places.
2
Harsh 25 26.5 28
Anurag 26 28 30
Harsh
get average marks for Harsh
"""
# n = int(input())
student_marks = {}
# for _ in range(n):
#     name, *line = input().split()
#     scores = list(map(float, line))
#     student_marks[name] = scores
student_marks['Harsh']=[25, 26.5, 28]
student_marks['Anurag']=[26,28,30]
query_name = "Harsh"
print("Student marks for",query_name)
avg=0
for x in student_marks:
    if x==query_name:
        sum=0
        marks=student_marks[x]
        for i in marks:
            sum+=i
        avg=sum/marks.__len__()
print('{0:.2f}'.format(avg))


print("Execute commands from list")
"""
insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
"""
commands=[
    'append 1',
    'append 6',
    'append 10',
    'append 8',
    'append 9',
    'append 2',
    'append 12',
    'append 7',
    'append 3',
    'append 5',
    'insert 8 66',
    'insert 1 30',
    'insert 6 75',
    'insert 4 44',
    'insert 9 67',
    'insert 2 44',
    'insert 9 21',
    'insert 8 87',
    'insert 1 75',
    'insert 1 48',
    'print',
    'reverse',
    'print',
    'sort',
    'print',
    'append 2',
    'append 5',
    'remove 2',
    'print'
]
lstData=[]
dt=0
idx=0
carr=[]
for x in commands:
    carr=x.split(" ")
    cmd=carr[0].__str__()
    # print(carr)
    if(cmd=='insert'):
        lstData.insert(int(carr[1]),int(carr[2]))
    elif(cmd=='print'):
        print(lstData)
    elif(cmd=='append'):
        lstData.append(int(carr[1]))
    elif(cmd=='remove'):
        lstData.remove(int(carr[1]))
    elif(cmd=='pop'):
        lstData.pop()
    elif(cmd=='sort'):
        lstData.sort()
    elif(cmd=='reverse'):
        lstData.sort(key=lambda x:x, reverse=True)
"""
list = []
print("Enter input")
n = int(input())
for i in range(n):
    a = input().split()
    if len(a) == 3:
        eval("list." + a[0] + "(" + a[1] + "," + a[2] + ")")
    elif len(a) == 2:
        eval("list." + a[0] + "(" + a[1] + ")")
    elif a[0] == "print":
        print(list)
    else:
        eval("list." + a[0] + "()")
"""

