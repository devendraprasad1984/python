import json

from flask import Flask
from flask import Response
from flask import request as req
from pymongo import MongoClient

app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST', 'OPTIONS'])
def login():
    return "got success"


@app.route('/')
def index():
    res = Response("")
    # setting CORS request handler
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res


@app.route('/test')
def test():
    return "Devednra welcome test!"


@app.route("/getDistinctStates", methods=['GET', 'POST', 'OPTIONS'])
def getDistinctStates():
    try:
        res = Response("")
        #        print(req.headers)
        con = MongoClient("mongodb://127.0.0.1:27017/")
        db = con.mydb
        states = {json.dumps(db.zips.distinct("state"))}
        #        res=Response(json.dumps(states))
        res = Response(states)
        #        res=Response(jsonify({'state':states}))
        res.headers['Access-Control-Allow-Origin'] = '*'
        return res
        con.close()
    except Exception as ex:
        print(ex)


@app.route('/zips', methods=['GET', 'POST', 'OPTIONS'])
def getZips():
    zips = []
    try:
        #        http://28.151.188.241:6290/getZipCodes?id=MA&city=METHUEN
        #        print(req.headers)
        #        print(json.dumps(req.args))
        con = MongoClient("mongodb://127.0.0.1:27017/")
        db = con.mydb
        if ("state" in req.args) and ("city" not in req.args):
            state = str(req.args["state"])
            stFltr = {"state": state}
            zipsData = db.zips.find(stFltr).sort("city")
        elif ("state" not in req.args) and ("city" in req.args):
            city = str(req.args["city"])
            ctFltr = {"city": city}
            zipsData = db.zips.find(ctFltr).sort("state")
        elif ("state" in req.args) and ("city" in req.args):
            state = str(req.args["state"])
            stFltr = {"state": state}
            zipsData = db.zips.find(stFltr).sort("city")
        elif ("state" not in req.args) and ("city" not in req.args):
            zipsData = []

        for zip in zipsData:
            zips.append(json.dumps(zip))
        #            data=str(zip["city"])+"|"+str(zip["loc"])+"|"+str(zip["pop"])
        con.close()
    except Exception as ex:
        print(ex)
    res = Response(json.dumps(zips))
    res.headers['Access-Control-Allow-Origin'] = '*'
    res.headers['mimetype'] = 'application/json'
    return res


@app.route('/zipsTable', methods=['GET', 'POST', 'OPTIONS'])
def getZipsTable():
    zips = []
    try:
        con = MongoClient("mongodb://127.0.0.1:27017/")
        db = con.mongoTraining
        if ("state" in req.args) and ("city" not in req.args):
            state = str(req.args["state"])
            stFltr = {"state": state}
            zipsData = db.zips.find(stFltr).sort("city")
        elif ("state" not in req.args) and ("city" in req.args):
            city = str(req.args["city"])
            ctFltr = {"city": city}
            zipsData = db.zips.find(ctFltr).sort("state")
        elif ("state" in req.args) and ("city" in req.args):
            state = str(req.args["state"])
            stFltr = {"state": state}
            zipsData = db.zips.find(stFltr).sort("city")
        elif ("state" not in req.args) and ("city" not in req.args):
            zipsData = []

        sDataTable = "<table>"
        for zip in zipsData:
            sDataTable += "<tr><td>" + zip["city"] + "</td><td>" + str(zip["pop"]) + "</td><td>" + str(
                zip["loc"]) + "</td></tr>"
        sDataTable += "</table>"
        zips.append(sDataTable)
        #            data=str(zip["city"])+"|"+str(zip["loc"])+"|"+str(zip["pop"])
        con.close()
    except Exception as ex:
        print(ex)
    res = Response(zips)
    res.headers['Access-Control-Allow-Origin'] = '*'
    res.headers['mimetype'] = 'application/html'
    return res


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=6200, debug=0)
