#Q. How would you optimally calculate p^k, where k is a non-negative integer? What is the complexity of the solution?

#A. First, let’s mention that the trivial solution has the complexity of O(k). The problem can be solved by squaring and multiplying.
# We know that p^k = p^x * p^y if x+y=k. We also know that p^k = (p^a)^b if a*b=k.
# For an even value of k, choosing a = 2 and b = k/2, thus having p^k = (p^2)^(k/2), will reduce the number of required multiplications almost in half. For an odd value of k, choosing x = 1 and y=k-1 will result in y being even, and we can then simply repeat the same process as for the even case. This allows us to define a recursive function:
# FUNCTION pow(base, exponent)
# IF exponent == 0
# RETURN 1
# ELSE IF exponent is even
# RETURN pow(base * base, exponent / 2)
# ELSE
# RETURN base * pow(base * base, (exponent - 1) / 2)
# END IF
# This solution results in a complexity of O(log k).

# import big_o
def approach1OfLoop(p,k):
    print("number to root: ",p,"number by root:",k)
    # loop over k times and multiply recursive p times
    res=1
    for i in range(int(k)):
        res=res*int(p)
    print("final values is ",res)

def approach2OfRecursive(p,k):
    res=0;
    if k == 0:
        res= 1
    elif k % 2==0:
        res= pow(p * p,k / 2)
    else:
        res= p * pow(p * p, (k - 1) / 2)
    print("the final value is: ",int(res))

p=input("enter number to square rooted")
k=input("enter number by which to square root")

if((p.isnumeric()==False) or (k.isnumeric()==False)):
    print("invalid input, please enter numeric value only")
else:
    # pos_i_gen= lambda n: big_o.datagen.integers(n, 0, 10000)
    p=int(p)
    k=int(k)
    print("solution for ",p,"^",k,"is")
    print("checking approach 1 of loop")
    approach1OfLoop(p,k)
    # best, others = big_o.big_o(approach1OfLoop(p,k),pos_i_gen, n_repeats=10)
    # print("big_o notation, algo complexity check",best)
    print("checking approach 2 of recusion")
    approach2OfRecursive(p,k)
