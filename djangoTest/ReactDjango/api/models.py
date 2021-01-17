from django.db import models

class Books(models.Model):
    title=models.TextField(max_length=100, null=False, blank=False)

