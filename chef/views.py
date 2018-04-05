from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from menu.models import FoodItem
from orders.models import Orders
from django.shortcuts import redirect
from django.db.models import Q
from waiter.models import Waiter
# Create your views here.
def chefview(request):
	orders_chef_view = []
	customer_orders = Orders.objects.filter(Q(status='N') | Q(status='C') )
	for o in customer_orders:
	 item = FoodItem.objects.get(id=o.food_id)
	 orders_chef_view.append({'id':o.id,'order':o.order_id,'food_name':item.name,'qty':o.qty,'status':o.status})
	return render(request,"chefview.html",{'chef':orders_chef_view})

def update(request,order_id):
	order = Orders.objects.filter(id=order_id)
	for o in order:
	 if o.status=='C':
	  Orders.objects.filter(id=order_id).update(status='D')
	  Waiter.objects.create_waiter_tasks('S',order_id,4,'N')
	 if o.status=='N':
	  Orders.objects.filter(id=order_id).update(status='C')
	return redirect('/chef/')