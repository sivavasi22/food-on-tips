from django.db import models

# Create your models here.


class Employee(models.Model):
	emp_choices = (
		('M','Manager'),
		('C','Chef'),
		('W','Waiter'),
		)
	emp_id = models.CharField(max_length=10)
	emp_pass = models.CharField(max_length=20)
	emp_type = models.CharField(max_length=1,choices=emp_choices)
	emp_firstname = models.CharField(max_length=50)
	emp_lastname = models.CharField(max_length=50)
	emp_hours = models.DecimalField(max_digits=4,decimal_places=2)
