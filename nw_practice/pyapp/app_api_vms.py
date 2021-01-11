from bottle import route, run, get, request, post

vms = [{"host_name": "gbmacvm01", "owner": 'dave', "qty": "1"}]


@route('/')
def hello():
    return 'hello world'


@get('/get_vms')
def get_vms_handler():
    return {"vms": vms}


@post('/new_vms')
def get_vms_handler():
    try:
        new_vms = [{"host_name": request.json.get('host_name'), "owner": request.json.get('owner'), "qty": request.json.get('qty')}]
        vms.append(new_vms)
        return {"vms": vms}
    except:
        return {'vms': request.json}


# curl -d '{"host_name":"gbmacvm02","owner":"devendra","qty":"3"}' -H "Content-Type:application/json" -X POST http://localhost:6200/new_vms -s

run(host='localhost', port=6200, debug=True, reloader=True)
