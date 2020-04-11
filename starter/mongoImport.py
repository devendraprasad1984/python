import json
import os

import pymongo


# factory class
class mainDataLoadClass:
    def __init__(self):
        print("Obj is " + objType)

    def __new__(cls, objType):
        if (objType == "file"):
            return loadJSONFile
        if (objType == "util"):
            return loadJsonViaMongoUtil


# class 1 for load data 2 file
class loadJSONFile:
    def loadData2MongoDB():
        oPath = "C:\\DEVEN\\RnD\\mongoDB\\"
        oFile = "AK.json"
        # import json into mongodb via pythong
        data = []
        con = pymongo.MongoClient('mongodb://28.151.188.241:6400/')
        db = con.mongoTraining
        db.city2.drop()
        print("Connected to " + db.name)
        with open(oPath + oFile) as fl:
            for line in fl:
                # print(line)
                doc = json.loads(line)
                db.city2.insert(doc)
                # data.append(line)
            fl.close()
        # print(str(data))
        # db.cityAK.insert(data)
        con.close()
        print("Dataset has been loaded")


# class 2 load data via utility
class loadJsonViaMongoUtil:
    def loadData2MongoDB():
        oName = "zips"
        oPath = "C:\\DEVEN\\RnD\\mongoDB\\dataset\\zips.json"
        path2MongoImportUtil = "c:\\mongo30\\bin\\mongoimport.exe"
        mongoServerRunningOn = " --host 28.151.188.241 --port 6400 "
        mongoDatabase = "mongoTraining"
        #    con = pymongo.MongoClient('mongodb://28.151.188.241:6200/')
        #    db = con.mongoTraining
        mongoCall2LoadJSON = path2MongoImportUtil + mongoServerRunningOn + "--db " + mongoDatabase + " --drop --collection " + oName + " --file " + oPath
        print("loading(" + oPath + ") of " + oName)
        print("command to run: " + mongoCall2LoadJSON)
        os.system(mongoCall2LoadJSON)
        #    print("Total "+str(db.zips.count())+" has been loaded")


# call methods
# objLoad=mainDataLoadClass("util")
objLoad = mainDataLoadClass("util")
objLoad.loadData2MongoDB()
