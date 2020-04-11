from collections import defaultdict

nums=defaultdict(int) #int is passed as the default_factory
nums["one"]=1
nums["two"]=1

# doesnt throw error if key doesnt exist
print(nums, nums["three"])


count=defaultdict(int)
names_list = "Mike John Mike Anna Mike John John Mike Mike Britney Smith Anna Smith".split()
for n in names_list:
    count[n]+=1

print("words counter",dict(count))



