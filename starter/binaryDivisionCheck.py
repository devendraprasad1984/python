# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010

bin_input="0100,0011,1010,1001"
divisor=5
print("binary input is",bin_input,"to be checked division by",divisor)
bin_in_arr=bin_input.split(',')
print(bin_in_arr)
new_div_arr=[]
for num in bin_in_arr:
    if int(num) % divisor ==0:
        new_div_arr.append(num)
print("new divisible numbers are",','.join(new_div_arr))


