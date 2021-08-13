from django.db import models

# Create your models here.
class CUSTOMERS(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=200, null=True)
    uid = models.CharField(max_length=30, null=True)
    age = models.IntegerField()
    loan_limit = models.DecimalField(max_digits=10, decimal_places=2)
    when = models.DateTimeField(auto_now_add=True, blank=True)

