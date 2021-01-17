from rest_framework import viewsets, authentication, permissions
from django.contrib.auth.models import User
from .models import Books
from .serializers import UserSerializer, BooksSerializer

class UserViewSets(viewsets.ModelViewSet):
    queryset = User.objects.all();
    serializer_class = UserSerializer

class BookViewSets(viewsets.ModelViewSet):
    queryset = Books.objects.all();
    serializer_class = BooksSerializer
    authentication_classes = [authentication.TokenAuthentication, ]
    permission_classes = [permissions.IsAuthenticated, ]


