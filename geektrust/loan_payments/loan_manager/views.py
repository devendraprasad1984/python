from django.shortcuts import render, HttpResponse as res
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def fn_LOAN(req):
    return res('LOAN')


@csrf_exempt
def fn_PAYMENT(req):
    return res('PAYMENT')


@csrf_exempt
def fn_BALANCE(req):
    return res('BALANCE')
