# Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world

inputData="hello world and practice makes perfect and hello world again"
w_arr=sorted(inputData.split(' '))
# w_arr.sort()
print(w_arr)
w_set=set()
for w in w_arr:
    w_set.add(w)
print("distinct words ordererd are")
print(sorted(w_set))
# print("distinct words ordererd are",sorted(w_set))


#sort-hand code
print(sorted(set(inputData.split(' '))))
