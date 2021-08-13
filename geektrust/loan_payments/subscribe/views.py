from django.shortcuts import render, HttpResponse as res
from django.http import HttpRequest
from loan_manager.common import config


# Create your views here.
def fn_GET_NEW_TOKEN(req: HttpRequest):
    return res('here is your new token')


def fn_SUBSCRIBE(req: HttpRequest):
    if req.method == config.GET:
        return res(config.NO_OP_ALLOWED)

    return res('subscription done. you secret key has been mailed')


def gn_GET_SUBSCRIBERS(req: HttpRequest):
    if req.method == config.POST:
        return res(config.NO_OP_ALLOWED)
    return res('here is your list')