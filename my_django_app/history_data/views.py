import json
from django.shortcuts import render, HttpResponse as res


def get_history_data(req):
    params = req.GET if req.method == 'GET' else req.POST
    paramObj = json.loads(json.dumps(params))
    id = paramObj['id']
    return res(
        json.dumps({
            "id": id,
            "msg": 'get_history_data',
            "status": 'success',
            "qur": paramObj
        }
        ), content_type='application/json')
