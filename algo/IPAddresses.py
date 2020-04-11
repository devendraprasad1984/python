"""
Program to generate all possible valid IP addresses from given string | Set 2
Given a string containing only digits, restore it by returning all possible valid IP address combinations.
A valid IP address must be in the form of A.B.C.D, where A, B, C and D are numbers from 0 – 255.
The numbers cannot be 0 prefixed unless they are 0.

Examples:

Input: str = “25525511135”
Output:
255.255.11.135
255.255.111.35

Input: str = “11111011111”
Output:
111.110.11.111
111.110.111.11

Approach: This problem can be solved using backtracking. In each call we have three options to create a single block of numbers of a valid ip address:

Either select only a single digit, add a dot and move onto selecting other blocks (further function calls).
Or select two digits at the same time, add a dot and move further.
Or select three consecutive digits and move for the next block.
At the end of the fourth block, if all the digits have been used and the address generated is a valid ip-address then add it to the results and then backtrack by removing the digits selected in the previous call.
"""

def validIP(arr=[],s_given="",idx=0,cnt=0,s_ip=""):
    if cnt==4 and s_given.__len__()==idx:
        arr.append(s_ip)
        return
    if s_given.__len__()<idx+1:
        return
    s_ip+=s_given[idx:idx+1]+'.'
    # Select one digit and call the
    validIP(arr,s_given,idx+1,cnt+1,s_ip)
    s_ip=s_ip[0:s_ip.__len__()-2]
    # Select two consecutive digits and call
    s_ip+=s_given[idx:idx+2]+'.'
    validIP(arr,s_given,idx+2,cnt+1,s_ip)
    s_ip=s_ip[0:s_ip.__len__()-3]
    #So we remove three index from the end
    if len(s_given)<idx+3:
        return
    s_ip+=s_given[idx:idx+3]+'.'
    validIP(arr,s_given,idx+3,cnt+1,s_ip)
    s_ip=s_ip[0:s_ip.__len__()-4]


if __name__ == '__main__':
    ipstr="25525511135"
    arr=[]
    n=[]
    validIP(arr,ipstr,0,0,"")
    for i in arr:
        n=i[0:len(i)-1].split(".")
        if int(n[0])>255 or int(n[1])>255 or int(n[2])>255 or int(n[3])>255:
            continue
        else:
            print(n,'.'.join(n))

