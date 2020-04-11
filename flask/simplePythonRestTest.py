# run as in cmd py simplePythonRestTest.py and call the url in browser
from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST', 'OPTIONS'])
def getHome():
    strRetVal = "I am Home"
    return strRetVal


@app.route('/login', methods=['GET', 'POST', 'OPTIONS'])
def getLogin():
    strRetVal = "I am login"
    return strRetVal


@app.route('/contacts', methods=['GET', 'POST', 'OPTIONS'])
def getContcts():
    strRetVal = "I am contacts"
    return strRetVal


@app.route('/data', methods=['GET', 'POST', 'OPTIONS'])
def getData():
    strRetVal = "I am data"
    return strRetVal


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=6200, debug=0)
