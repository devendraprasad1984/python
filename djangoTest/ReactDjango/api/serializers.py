from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Books

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','password']
        extra_kwargs={'password':{'write_only':True, 'required':True}} # hides returing of password in api calls

    def create(self, validate_data):
        user=User.objects.create_user(**validate_data) #helps in password getting hashed
        Token.objects.create(user=user)
        return user

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model=Books
        fields=['title']


