from django.db import models

# Create your models here.
from django.db import models

class Customer(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    mobileno=models.CharField(max_length=50)
    image=models.CharField(max_length=1000)
    email=models.CharField(max_length=100)

class mobile(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
