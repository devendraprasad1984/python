from django.http import HttpResponse as res, HttpRequest
from django.shortcuts import render, redirect
from . import models

redirectUrlMainPage = '/todos/view/'
todoDB = 'todos'


def getTodoList():
    tododata=models.Todo.objects.using(todoDB).all()
    return tododata


def todo_list_view(req):
    return render(req, 'todos/index.html', {'todo_list':getTodoList()})


def todo_list(req):
    list = getTodoList()
    return res(list)


def insert_todo_item(req: HttpRequest):
    name = req.POST['name']
    obj = models.Todo(content=name)
    obj.save(using=todoDB)
    return redirect(redirectUrlMainPage)


def delete_todo_item(req,todo_id):
    obj = models.Todo.objects.using(todoDB).get(id=todo_id)
    obj.delete()
    return redirect(redirectUrlMainPage)
