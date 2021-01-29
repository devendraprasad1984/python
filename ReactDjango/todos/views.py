from django.http import HttpResponse as res, HttpRequest
from django.shortcuts import render, redirect
from . import models
from django.core import serializers
import json

# from django.forms.models import model_to_dict


redirectUrlMainPage = '/todos/view/'
todoDB = 'todos'
jsonType = 'application/json'


def serialise(data, flds):
    objx = serializers.serialize('json', data, fields=flds)
    return objx


def simple_serialise(data, flds):
    jsonObj = json.loads(serializers.serialize('json', data, fields=flds))
    for d in jsonObj:
        del d['model']
    return json.dumps(jsonObj)


def getTodoList():
    tododata = models.Todo.objects.using(todoDB).all()
    return tododata


def todo_list_view(req):
    return render(req, 'todos/index.html', {'todo_list': getTodoList()})


def todo_list(req):
    flds = ['content']
    # obj = serialise(getTodoList(), flds)
    obj1 = simple_serialise(getTodoList(), flds)
    # listJson = {'data': obj}
    return res(obj1, content_type=jsonType)
    # return json.dumps(obj)


def insert_todo_item(req: HttpRequest):
    name = req.POST['name']
    obj = models.Todo(content=name)
    obj.save(using=todoDB)
    return redirect(redirectUrlMainPage)

def add_todo(req,name):
    obj = models.Todo(content=name)
    obj.save(using=todoDB)
    return 'saved'


def delete_todo_item(req, todo_id):
    obj = models.Todo.objects.using(todoDB).get(id=todo_id)
    obj.delete()
    return redirect(redirectUrlMainPage)
