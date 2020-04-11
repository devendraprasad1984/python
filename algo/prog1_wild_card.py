"""
Replace wild cards with all possible combinations of zeros and ones
0?1?

This algorithm runs in O(2n) time where n is equal to the number of wildcards because there are 2n
possible sets for all wildcards in the string. The algorithm must perform this many steps to calculate all the sets.
[1] If there are no wildcards in the string, then the algorithm runs in linear time, O(n), because it will simply
append each character to a string.

"""

def sprint(nstr=[],i=0):
    if i==nstr.__len__():
        print(''.join([str(x) for x in nstr]))
        return

    if nstr[i]=='?':
        nstr[i]=0
        sprint(nstr,i+1)
        nstr[i]=1
        sprint(nstr,i+1)
        nstr[i]='?'
    else:
        sprint(nstr,i+1)

str1="0?1?"
print("new string for",str1)
sarr=[x for x in str1]
sprint(sarr,0)

str1="1??0?101"
print("new string for",str1)
sarr=[x for x in str1]
sprint(sarr,0)




