#0/1 knapsack
# items=[(index,weight,value)], tuple to hold this structure
# using knapsack algo we need maximize the value within limit of weight being assigned as the capacity

from random import random
def build_items(num_of_items_tuple):
    res=[]
    max_num=100
    for i in range(num_of_items_tuple):
        res.append((i,1+int(max_num*random()),1+int(max_num*random())))
    return res

def generatePowerSetOfItems(items):
    res=[[]]
    for item in items:
        newset=[r+[item] for r in res]
        res.extend(newset)
    return res

# try each and every subset in set
# this solution is not optimal for large list, hence dynamic programming need to find optimal solutions
def knapsack_using_bruteforce(items,max_weight):
    knapsack=[]
    best_value=0
    best_weight=0
    for item_set in generatePowerSetOfItems(items):
        # print("working on itemset",item_set)
        set_weight=sum([e[1] for e in item_set])
        set_value=sum([e[2] for e in item_set])
        if set_weight<=max_weight and set_value>best_value:
            best_value=set_value
            best_weight=set_weight
            knapsack=item_set
    return knapsack,best_weight,best_value

def sort_on_weight(item):
    return item[1]
def sort_on_value(item):
    return item[2]
def sort_on_density(item):
    return float(item[2])/item[1]

# this will sort and keep checking and stops as soon as sum exceeds
def knapsack_using_greedy(items,max_weight,keyFunc=sort_on_value):
    knapsack=[]
    knapsack_weight=0
    knapsack_value=0
    items_sorted=sorted(items,key=keyFunc)
    while len(items_sorted)>0:
        item=items_sorted.pop()
        if sort_on_weight(item)+knapsack_weight<=max_weight:
            knapsack.append(item)
            knapsack_weight+=sort_on_weight(item)
            knapsack_value+=sort_on_value(item)
        else:
            break
    return knapsack,knapsack_weight,knapsack_value


num_of_items=150
data=build_items(num_of_items)
print("computing powersets",2**num_of_items)
print("data items are having(index,weight,size)\n",data)

# powersetOfItems=generatePowerSetOfItems(data)
# print("the powserset of above data is\n",powersetOfItems)
# knapsack_res,best_weight,best_value=knapsack_using_bruteforce(powersetOfItems,100)
# knapsack_res=knapsack_using_bruteforce(data,100)

knapsack_res=knapsack_using_greedy(data,100,sort_on_weight)
print("knapsack result sorted on weight is\n",knapsack_res)
knapsack_res=knapsack_using_greedy(data,100,sort_on_value)
print("knapsack result sorted on value is\n",knapsack_res)
knapsack_res=knapsack_using_greedy(data,100,sort_on_density)
print("knapsack result sorted on density is\n",knapsack_res)
# print("knapsack result is\n",knapsack_res,"\nbest weight",best_weight,"\nbest value",best_value)
