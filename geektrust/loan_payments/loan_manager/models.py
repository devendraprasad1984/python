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
    bankid = models.ForeignKey(BANKS, to_field='id', on_delete=models.CASCADE)
    customerid = models.ForeignKey(CUSTOMERS, to_field='id', on_delete=models.CASCADE)
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    rate = models.DecimalField(max_digits=5, decimal_places=2)
    period = models.IntegerField()
    period_months = models.IntegerField()
    repaid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    emi_amount = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount_PI = models.DecimalField(max_digits=10, decimal_places=2)


class QUERY_LOG(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    type = models.CharField(max_length=50)
    log = models.TextField()
    when = models.DateTimeField()
