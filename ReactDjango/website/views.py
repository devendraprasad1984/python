# from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render
from django.views.generic.base import TemplateView

# def index1(req):
#     template=loader.get_template('index.html')
#     return HttpResponse(template.render({},req))
    # return HttpResponse('Hello Welcome to Django website modules! fine lets go ahead.')

def home(request):
    return render(request,'home.html',{})

def about(request):
    return render(request,'about.html',{})

def contact(request):
    return render(request,'contactus.html',{})

class ProfileView(TemplateView):
    template_name = 'accounts/profile.html'

