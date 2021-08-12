import json

from django.shortcuts import render
from django.http import HttpResponse as res, HttpRequest


# from my_django_app.common import constants


def get_history_data(req: HttpRequest):
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
