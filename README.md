# Ex02 Django ORM Web Application
## Date:  12.11.2024 

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM

![ormimg](https://github.com/user-attachments/assets/ff50dbd9-2784-4147-92c7-1e45125c0514)



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
.....
admin.py

from django.contrib import admin
from .models import BankLoan,BankLoanAdmin
admin.site.register(BankLoan,BankLoanAdmin)

models.py

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
......

## OUTPUT
![alt text](<orm bank.png>)
Include the screenshot of your admin page.


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
