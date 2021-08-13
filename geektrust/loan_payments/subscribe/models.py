from django.db import models


# Create your models here.
class SUBSCRIPTION(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    email = models.EmailField(null=False, unique=True)
    secret_key = models.TextField(null=True)
    when = models.DateTimeField(auto_now_add=True, blank=True)

