from rest_framework import viewsets, authentication, permissions
from django.contrib.auth.models import User
from . import models
from . import serializers

class UserViewSets(viewsets.ModelViewSet):
    queryset = User.objects.all();
    serializer_class = serializers.UserSerializer

class BookViewSets(viewsets.ModelViewSet):
    queryset = models.Books.objects.all();
    serializer_class = serializers.BooksSerializer
    authentication_classes = [authentication.TokenAuthentication, ]
    permission_classes = [permissions.IsAuthenticated, ]

# class TaskViewSets(viewsets.ModelViewSet):
#     queryset = models.Task.objects.all();
#     serializer_class = serializers.TaskSerializer
#     # authentication_classes = [authentication.TokenAuthentication, ]
#     # permission_classes = [permissions.IsAuthenticated, ]
