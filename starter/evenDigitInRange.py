# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.

# method1
print("method1 excluding 2 & 1 only and 0's")
def isPrime(num):
    flag=True
    if num<2:
        flag=False
    for i in range(2,num):
        if num%i ==0:
            flag=False
            break
    return flag

num_range=[x for x in range(1000,3001)]
print("prime numbers are")
prime_num=[]
all_prime_digits=[]
for x in num_range:
    if isPrime(x)==True:
        prime_num.append(str(x))

    all_digit_flag=True
    for y in str(x):
        if isPrime(int(y))==False:
            all_digit_flag=False
            break
    if all_digit_flag==True:
        all_prime_digits.append(str(x))

print(','.join(prime_num))
print("all prime digits are")
print(','.join(all_prime_digits))


# method2
print("method2")
values = []
for i in range(1000, 3001):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        values.append(s)
print(",".join(values))