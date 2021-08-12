from django.shortcuts import render, HttpResponse as res


# Create your views here.
def index(req):
    return res('my base')


def home(req):
    return res('my home')


def about(req):
    return res('my about')


def services(req):
    return res('my services')


def contactus(req):
    return res('my contactus')
