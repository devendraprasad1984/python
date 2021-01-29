from django.http import HttpResponse as res
from django.shortcuts import render

# @api_view(['GET'])
def todo_list(req):
    return res('from todos url')

def todo_list_view(req):
    return render(req,'todos/index.html')
