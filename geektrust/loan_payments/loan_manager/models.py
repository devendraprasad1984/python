from django.db import models


class BANKS(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    uid = models.CharField(max_length=20)
    name = models.CharField(max_length=100)


class CUSTOMERS(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    loan_limit = models.DecimalField(max_digits=10, decimal_places=2)


class LOANS(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    uid = models.CharField(max_length=20)
    bankid = models.ForeignKey(BANKS, on_delete=models.CASCADE)
    customerid = models.ForeignKey(CUSTOMERS, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    rate = models.DecimalField(max_digits=5, decimal_places=2)
    period = models.IntegerField()
    repaidAmout = models.DecimalField(max_digits=10, decimal_places=2)
