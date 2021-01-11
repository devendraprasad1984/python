from bottle import route, run


@route('/')
def main():
    return "HelloWorld from main app api"

run(host='localhost',port=6200,debug=True,reloader=True)

