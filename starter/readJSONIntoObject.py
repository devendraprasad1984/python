import json

myFilePath="testLoad.json"
fl=open(myFilePath)
print('reading all lines at once')
allLines=fl.readlines()
print(allLines)

fl.seek(0)
jsonData=json.load(fl)
print('converted json data')
print(jsonData)

# fl.seek(0)
# print('reading lines one by one')
# while True:
#     line=fl.readline()
#     if len(line) == 0:
#         break
#     print(line)
fl.close()

print("read a field from json object",jsonData["etag"])
# loop over json object loaded from file, it is called dictionary object
for k,v in jsonData.items():
    print(k,v)
    if isinstance(v,list):
        for k in v:
            if isinstance(k,dict):
                for i,j in k.items():
                    print(i,j)

