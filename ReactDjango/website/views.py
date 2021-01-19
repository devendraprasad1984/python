# from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# def index1(req):
#     template=loader.get_template('index.html')
#     return HttpResponse(template.render({},req))
#     return HttpResponse('Hello Welcome to Django website modules! fine lets go ahead.')

def home(request):
    print('loggedin user', request.user)
    return render(request,'home.html',{})

def about(request):
    return render(request,'about.html',{})

def contact(request):
    return render(request,'contactus.html',{})

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'

