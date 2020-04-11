from collections import Counter

# myList = [1, 1, 2, 3, 4, 5, 3, 2, 3, 4, 2, 1, 2, 3]
# ctr = Counter(myList)
# print(ctr.items(), ctr.keys(), ctr.values())

"""
Task: is a shoe shop owner. His shop has  number of shoes. 
He has a list containing the size of each shoe he has in his shop. 
There are  number of customers who are willing to pay  amount of money only if they get the shoe of their desired size.
Your task is to compute how much money  earned.
Input Format: The first line contains , the number of shoes. 
    The second line contains the space separated list of all the shoe sizes in the shop.
    The third line contains , the number of customers. 
    The next  lines contain the space separated values of the  desired by the customer and , the price of the shoe.
Output Format: Print the amount of money earned by .
"""

# shoes = int(input())
# sizes = list(map(int,input().split()))
# cust = int(input())
# demand = []
# for i in range(cust):
#     demand.append(list(input().split()))
#


shoes = 10
sizes = [2, 3, 4, 5, 6, 8, 7, 6, 5, 18]
cust = 6
demand = []
demand.append([6, 55])
demand.append([6, 45])
demand.append([6, 55])
demand.append([4, 40])
demand.append([18, 60])
demand.append([10, 50])
money=0
sizesCounter=dict(Counter(sizes))
print(sizesCounter)
for x in demand:
    print(x[0],x[0] in sizesCounter)
    k=int(x[0])
    if k in sizesCounter:
        sizesCounter[k]-=1
        if(sizesCounter[k]>=0):
            money+=int(x[1])
            print(sizesCounter)
    # print(x[0],x[1])
print("money earned",money)
