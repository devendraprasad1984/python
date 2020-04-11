#Q. A numeric array of length N is given. We need to design a function that finds all positive numbers in the array that have their opposites in it as well. Describe approaches for solving optimal worst case and optimal average case performance, respectively.

#A. Let us first design an approach with optimal worst case time.
# We need to compare numbers to see if they have their opposites in the array. The trivial solution of comparing all numbers has a consistent time of O(N^2). The great number of comparisons involved should suggest trying to establish a total order operator that allows us to use sorting for solving the problem. If we define a comparison operator that places all instances of a number right after all instances of its opposite, we would have exactly pair of consecutive opposite numbers for each number that has its opposite in the array.
# An example of what we want to achieve:
# Array: -7 4 -3 2 2 -8 -2 3 3 7 -2 3 -2
# Sorted: -2 -2 -2 2 2 -3 3 3 4 -7 7 -8
# We see that after our special sorting method, we have [-2, 2], [-3, 3] and [-7, 7] combinations happening consecutively exactly once. Implementing this comparison is simple and it can be implemented as follows.
#
# FUNCTION compare(a, b)
# IF a != b and a != -b
# RETURN abs(a) < abs(b)
# ELSE
# RETURN a < b
# If the numbers aren’t equal or opposite, we sort them by their absolute value, but if they are, we sort them by their sign. Finally, a solution based on this is now very simple:
#
# FUNCTION find_numbers_with_opposites(numbers)
# answer = List
# sorted_numbers = sort_by(numbers, compare)
# FOR n IN [1..sorted_numbers.length()]
# IF sorted_numbers[n] > 0 AND sorted_numbers[n - 1] == -sorted_numbers[n]
# answer.push(n)
# END IF
# END FOR
# RETURN answer
# This implementation has a worst case runtime complexity of O(N log N), with the sorting algorithm being the bottleneck.
# Optimal average case time complexity of O(N) can be achieved using Hash Tables. We map numbers to their absolute values, and check if their opposites are already in the Hash Table.
#
# FUNCTION find_numbers_with_opposites(numbers)
# table = HashTable<number, number>
# answer = List
# FOR number IN numbers
# IF number == 0
# CONTINUE
# END IF
# key = abs(number)
# IF key not in table
# table[key] = number
# ELSE IF table[key] = -number
# answer.push(key)
# table[key] = 0
# END IF
# END FOR
# We change the value in the table to something that will never be equal to any of the numbers in the array so we don’t return duplicate results from duplicate matches.
# All HashTable operations have an average time complexity of O(1), and our complexity is a result of performing operations N times.

def approach1OfSimpleLoops():
    givenArray=[-7, 4, -3, 2, 2, -8, -2, 3, 3, 7, -2, 3, -2]
    print("given array is",givenArray)
    posArray=[]
    negArray=[]
    for i in givenArray:
        if i>0:
            posArray.insert(posArray.__len__(),i)
        else:
            negArray.insert(negArray.__len__(), i)
    print("positive array",posArray,"negative array",negArray)
    # loop over positive to check in existence negative array and if found, push to final array
    finalArray=[]
    for i in posArray:
        if negArray.__contains__(-i):
            finalArray.insert(finalArray.__len__(),i)
    print("final values of positive elements that has equivalent negative counterpart also available is: ",finalArray)

approach1OfSimpleLoops()


