
# check index in array
def  findNumber(arr, k):
    found=k in arr
    if(found==False):
        return "NO"
    else:
        return "YES"

x=['a', 'b', 'new', 'mpilgrim', 'z', 'example', 'new', 'two', 'elements']
# print("element found: "+str(findNumber(x,'example1')));

def  oddNumbers(l, r):
    for i in range(l,r):
        if(i%2!=0):
            print(i)

# oddNumbers(3,9)



def cleanString(sData):
    openBracketChar="("
    closeBracketChar=")"
    newString=""
    foundOpenFirst=False
    foundOpen=False
    foundClose=False
    nonNumericCharPos={};
    for i in range(len(sData)):
        if(sData[i]==openBracketChar):
            foundOpen=True
            foundOpenFirst=True
        elif(sData[i]==closeBracketChar):
            foundClose=True
        else:
            nonNumericCharPos.update({i:sData[i]})
            # newString+=sData[i]


        if(foundOpenFirst==True and foundOpen==True and foundClose==True):
            newString+=openBracketChar+closeBracketChar
            # newString+=openBracketChar+sData[i]
            foundOpenFirst=False
            foundOpen=False
            foundClose=False

    # loop and insert non expression char at their position in string
    for key,value in nonNumericCharPos.items():
        newString=newString[:key]+value+newString[key:]

    listOfChars=list(newString)
    print(listOfChars)

    return newString

sData="(x)())()"
newData = cleanString(sData)
print(newData)

