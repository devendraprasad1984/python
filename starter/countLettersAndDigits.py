# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3

input_string="Hello world! 123"
obj_dic={'letters':0, 'digits':0, 'lower':0, 'upper':0}
for x in input_string:
    if x.isalnum():
        obj_dic['letters']+=1
    if x.isdigit():
        obj_dic['digits']+=1
    if x.isupper():
        obj_dic['upper']+=1
    if x.islower():
        obj_dic['lower']+=1

print(obj_dic,"letters are",obj_dic['letters'],"digits are",obj_dic['digits'])
print("upper are",obj_dic['upper'],"lower",obj_dic['lower'])
