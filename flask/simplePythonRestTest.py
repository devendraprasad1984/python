# run as in cmd py simplePythonRestTest.py and call the url in browser
from flask import Flask, make_response, jsonify
from flask_httpauth import HTTPBasicAuth
# from requests.auth import HTTPBasicAuth
import requests


# https://www.pluralsight.com/guides/web-scraping-with-request-python
app = Flask(__name__)
auth = HTTPBasicAuth()
supported_methods=['GET', 'POST', 'OPTIONS']

@auth.get_password
def get_password(username):
    if username == 'dp':
        return 'admin'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

# curl -i http://localhost:6200/
# curl -u miguel:python -i http://localhost:6200/
@app.route('/', methods=supported_methods)
@auth.login_required
def getHome():
    strRetVal = "I am Home"
    return strRetVal


@app.route('/login', methods=supported_methods)
@auth.login_required
def getLogin():
    strRetVal = "I am login"
    return strRetVal


@app.route('/contacts', methods=supported_methods)
def getContcts():
    strRetVal = "I am contacts"
    return strRetVal


@app.route('/data', methods=supported_methods)
def getData():
    strRetVal = "I am data"
    return strRetVal

# consume a rest api
@app.route('/rest',methods=supported_methods)
def getEmps():
    uri='http://dummy.restapiexample.com/api/v1/employees'
    data=requests.get(uri)
    return data.json()

@app.route('/todo/<id>',methods=supported_methods)
def getTodo(id):
    uri='https://jsonplaceholder.typicode.com/todos/'+id
    data=requests.get(uri)
    # print(data.text)
    return data.json()

@app.route('/posts',methods=supported_methods)
def getPosts():
    data = {'title':'Pyton Requests','body':'Requests are qwesome','userId':1}
    url='https://jsonplaceholder.typicode.com/posts'
    res=requests.post(url,data,stream=True)
    # response.iter_content(chunk_size=1024)
    return res.raw.read(100)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=6200, debug=0)

