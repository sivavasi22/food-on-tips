from django.db import models
#from menu.models import FoodItem
# # Create your models here.
class OrderManager(models.Manager):
	def create_order(self,oID,ID,Q,s):
		order = self.create(order_id=oID,food_id=ID,qty=Q,status=s)
		return order

class Orders(models.Model):
	status_choice = (
		('N','New Order'),
		('C','Cooking'),
		('D', 'Done'),
		)
	order_id = models.IntegerField()
	food_id = models.IntegerField()
	qty = models.IntegerField()
	status = models.CharField(max_length=1,choices=status_choice)
	objects = OrderManager()