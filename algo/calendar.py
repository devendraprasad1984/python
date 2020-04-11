# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
ip = input().split()
m = int(ip[0])
d = int(ip[1])
y = int(ip[2])
caldays=list(calendar.day_name)
wk=[calendar.weekday(y, m, d)][0]
print(caldays[wk].upper())
