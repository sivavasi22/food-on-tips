from django.db import models

# Create your models here.
class WaiterManager(models.Manager):
	def create_waiter_tasks(self,tsk,ord_id,tab,stat):
		waiter_task = self.create(task = tsk, order_id=ord_id, table=tab, status=stat)
		return waiter_task
		
class Waiter(models.Model):
	task_choices=(
		('C','Clean Table'),
		('S','Serve'),
		)
	status_choices = (
		('A','Attended'),
		('N','Not Attended'),
		)
	task = models.CharField(max_length=1,choices=task_choices)
	order_id = models.IntegerField()
	table = models.IntegerField()
	status = models.CharField(max_length=1,choices=status_choices)
	objects = WaiterManager()