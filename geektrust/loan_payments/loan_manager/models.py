from django.db import models
import datetime


class BANKS(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    uid = models.CharField(max_length=30, null=True)
    name = models.CharField(max_length=100, null=True)
    when = models.DateTimeField(default=datetime.datetime.now())


class CUSTOMERS(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=200, null=True)
    uid = models.CharField(max_length=30, null=True)
    age = models.IntegerField()
    loan_limit = models.DecimalField(max_digits=10, decimal_places=2)
    when = models.DateTimeField(default=datetime.datetime.now())


class LOANS(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    uid = models.CharField(max_length=30, null=True)
    bankid = models.ForeignKey(BANKS, to_field='id', on_delete=models.CASCADE)
    customerid = models.ForeignKey(CUSTOMERS, to_field='id', on_delete=models.CASCADE)
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    rate = models.DecimalField(max_digits=5, decimal_places=2)
    period = models.IntegerField()
    period_months = models.IntegerField()
    repaid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    emi_amount = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount_PI = models.DecimalField(max_digits=10, decimal_places=2)
    when = models.DateTimeField(default=datetime.datetime.now())


class QUERY_LOG(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    type = models.CharField(max_length=50)
    log = models.TextField()
    when = models.DateTimeField(default=datetime.datetime.now())
