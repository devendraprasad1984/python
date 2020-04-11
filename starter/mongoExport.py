import json

from pymongo import MongoClient


def export2JSON():
    con = MongoClient('mongodb://28.151.188.241:6200/')
    db = con.mongoTraining
    states = db.zips.distinct("state")
    print(json.dumps(states))
    sName = input("Enter State Name: ")

    fltr = {"state": sName}
    zips = db.zips.find(fltr).sort("city")

    oPath = "C:\\xampp\\htdocs\\lite\\mongoOutput\\" + sName + ".json"
    with open(oPath, "w") as fl:
        for zip in zips:
            #            print(json.dumps(zip))
            #            print(str(zip["city"])+"|"+str(zip["loc"])+"|"+str(zip["pop"]))
            #            fl.write(json.dumps(zip))
            fl.write(str(zip))
    fl.close()
    con.close()
    print("Data has been exported to " + oPath)


export2JSON()
