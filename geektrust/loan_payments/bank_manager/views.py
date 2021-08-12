from django.shortcuts import render, HttpResponse as res
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def fn_ADD_BANK(req):
    return res('bank added')
