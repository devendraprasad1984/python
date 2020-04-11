# Question:
# Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
# D 100
# W 200
# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500

import math, random

input_data=[]
account={'D':0,'W':0}
# setting up input for deposits and withdrawals
for i in range(1,100):    
    x=str(round(random.randint(i,1000)))
    input_data.append("D "+x)
    x=str(round(random.randint(i,500)))
    input_data.append("W "+x)
print("total accounting entries")
print(','.join(input_data))

print("calculating account balance")
account_bal=0
for d in input_data:
    tmp_arr=d.split(' ')
    account[tmp_arr[0]]+=float(tmp_arr[1]) if tmp_arr[0]=='D' else -float(tmp_arr[1])

account_bal=account['D']+account['W']
print("account object holding total debits and credits",account)
print("consolidated account balance is", account_bal)
