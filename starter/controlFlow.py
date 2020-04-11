x = -6  # Branching
if x > 0:  # If
    print("Positive")
elif x == 0:  # Else if AKA elseif
    print("Zero")
else:  # Else
    print("Negative")

list1 = [100, 200, 300]
for i in list1: print(i)  # A for loop

for i in range(0, 5): print(i)  # A for loop from 0 to 4

for i in range(5, 0, -1): print(i)  # A for loop from 5 to 1

for i in range(0, 5, 2): print(i)  # A for loop from 0 to 4, step 2

list2 = [(1, 1), (2, 4), (3, 9)]
for x, xsq in list2: print(x, xsq)  # A for loop with a two-tuple as its iterator

l1 = [1, 2];
l2 = ['a', 'b']
for i1, i2 in zip(l1, l2): print(i1, i2)  # A for loop iterating two lists at once.

i = 5
while i > 0:  # A while loop
    i -= 1

list1 = ["cat", "dog", "mouse"]
i = -1  # -1 if not found
for item in list1:
    i += 1
    if item == "dog":
        break  # Break; also usable with while loop
print("Index of dog:", i)
for i in range(1, 6):
    if i <= 4:
        continue  # Continue; also usable with while loop
    print("Greater than 4:", i)

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n / x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
