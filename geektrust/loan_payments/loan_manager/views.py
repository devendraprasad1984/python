from django.shortcuts import render, HttpResponse as res


# Create your views here.
def fn_LOAN(req):
    return res('LOAN')


def fn_PAYMENT(req):
    return res('PAYMENT')


def fn_BALANCE(req):
    return res('BALANCE')
