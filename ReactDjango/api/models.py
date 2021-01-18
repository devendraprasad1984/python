from django.db import models

class Books(models.Model):
    title=models.TextField(max_length=100, null=False, blank=False)

class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.title
