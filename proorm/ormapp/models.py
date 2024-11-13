from django.db import models
from django.contrib import admin
class BankLoan (models.Model):
    loan_id=models.IntegerField(primary_key=True)
    loan_type=models.CharField(max_length=30)
    loan_amd=models.FloatField()
    cust_acno=models.IntegerField()
    cust_name=models.CharField(max_length=50)
 
class BankLoanAdmin(admin.ModelAdmin):
    list_display=('loan_id','loan_type','loan_amd','cust_acno','cust_name')