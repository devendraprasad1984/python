from django.db import models


# class is like a db table and its properties are like columns inside that table
class Todo(models.Model):
    content = models.TextField()
