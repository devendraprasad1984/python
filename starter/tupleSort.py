# You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:
# 1: Sort based on name;
# 2: Then sort based on age;
# 3: Then sort by score.
# The priority is that name > age > score.
# If the following tuples are given as input to the program:
# Tom,19,80
# John,20,90
# Jony,17,93
# Json,21,85
# Then, the output of the program should be:
# [(John, 20, 90), (Jony, 17, 91), (Jony, 17, 93), (Json, 21, 85), (Tom, 19, 80)]
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
# We use itemgetter to enable multiple sort keys.

# from operator import itemgetter,attrgetter

print("input name,age,height in form of tuples input")
input_data=[]
input_data.append("Tom,19,80")
input_data.append("Jony,17,93")
input_data.append("Json,21,85")
input_data.append("John,20,90")
input_data.append("Jony,17,91")
# convert string into tuples object
# input_tuples_array=[tuple(map(str,x[1:-1].split(,))) for x in input_data]
print("input data is ",input_data)
input_tuples_array=[tuple(x[0:len(x)].split(',')) for x in input_data]
print("input tuples are", input_tuples_array)
for t in input_tuples_array:
    print(t,t[0],t[1],t[2])

sorted_tup=sorted(input_tuples_array,key=lambda x: (x[0],x[1],x[2]))
print(sorted_tup)

