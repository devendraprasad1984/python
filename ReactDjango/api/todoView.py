from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models
from . import serializers

#more manageable view function based than viewsets
@api_view(['GET'])
def apiOverview(req):
    api_urls = {
        'List': '/tast-list/',
        'Detail View': '/task-detail/<str:pk>/',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def taskList(req):
    tasks = models.Task.objects.all().order_by('-id')
    ser = serializers.TaskSerializer(tasks, many=True)
    return Response(ser.data)

@api_view(['GET'])
def taskDetail(req,pk):
    tasks=models.Task.objects.get(id=pk)
    ser=serializers.TaskSerializer(tasks, many=False)
    return Response(ser.data)

@api_view(['POST'])
def taskCreate(req):
    ser=serializers.TaskSerializer(data=req.data)
    if ser.is_valid():
        ser.save()
    return Response(ser.data)

@api_view(['POST'])
def taskUpdate(req, pk):
    task=models.Task.objects.get(id=pk)
    ser=serializers.TaskSerializer(instance=task, data=req.data)
    if ser.is_valid():
        ser.save()
    return Response(ser.data)

@api_view(['DELETE'])
def taskDelete(req, pk):
    task=models.Task.objects.get(id=pk)
    task.delete()
    return Response('Item deleted successfully')
