# from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render

# def index1(req):
#     template=loader.get_template('index.html')
#     return HttpResponse(template.render({},req))
    # return HttpResponse('Hello Welcome to Django website modules! fine lets go ahead.')

def home(req):
    return render(req,'home.html',{})

def about(req):
    return render(req,'about.html',{})

def contact(req):
    return render(req,'contactus.html',{})
