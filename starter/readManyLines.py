# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:

print("read multiple lines")
lines=[]
while True:
    s=input()
    if len(s)==0:
        break
    lines.append(s.upper())

for l in lines:
    print(l)


