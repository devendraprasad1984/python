from django.db import models
from bank_manager import models as bank
from customer_manager import models as customer


class LOANS(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    uid = models.CharField(max_length=30, null=True)
    bankid = models.ForeignKey(bank.BANKS, to_field='id', on_delete=models.CASCADE)
    customerid = models.ForeignKey(customer.CUSTOMERS, to_field='id', on_delete=models.CASCADE)
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    rate = models.DecimalField(max_digits=5, decimal_places=2)
    period = models.IntegerField()
    period_months = models.IntegerField()
    repaid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    emi_amount = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount_PI = models.DecimalField(max_digits=10, decimal_places=2)
    when = models.DateTimeField(auto_now_add=True, blank=True)


class QUERY_LOG(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    type = models.CharField(max_length=50)
    log = models.TextField()
    when = models.DateTimeField(auto_now_add=True, blank=True)
