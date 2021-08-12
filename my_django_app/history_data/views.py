import json

from django.shortcuts import render
from django.http import HttpResponse as res
# from ..common import constants

# Create your views here.

def get_history_data(req):
    return res(json.dumps({"msg":'Hello', "status":'success'}), content_type='application/json')
