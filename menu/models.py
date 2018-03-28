from django.db import models

# Create your models here.
class FoodItem(models.Model):
	FoodChoice = (
		('V','Veg'),
		('N','Non -Veg'),
		)
	choice = models.CharField(max_length=1, choices=FoodChoice)
	name = models.CharField(max_length=50)
	price = models.DecimalField(max_digits=5,decimal_places=2)
	cusine = models.CharField(max_length=20)
	def get_item_name():
		return name