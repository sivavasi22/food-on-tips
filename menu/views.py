from django.shortcuts import render
from django.http import HttpResponse
from . models import FoodItem
from orders.models import Orders
from django.db.models import Q
from django.forms.formsets import formset_factory
from django.contrib import messages
#from django.core.urlresolvers import reverse
import random

# Create your views here.
def menu(request):
	if request.method == 'POST':
		order_req=request.POST.getlist('order[]')
		r = random.randint(1000,9999)
		bill = []
		for id in order_req:
			s = 'order_qty['+id+']'
			order_qty=request.POST.get(s)
			Orders.objects.create_order(r,id,order_qty,'N')
		customer_orders = Orders.objects.filter(order_id=r )
		total = 0
		for o in customer_orders:
			item = FoodItem.objects.get(id=o.food_id)
			total = total + o.qty*item.price
			print(item.name)
			bill.append({'order':o.order_id,'food_name':item.name,'qty':o.qty,'price':item.price,'subtotal':o.qty*item.price})
		return render(request,"bill.html",{'bill':bill,'total':total})
	else:
		all_entries = FoodItem.objects.all().order_by('cusine','-choice')		
		return render(request, "menu.html",{'menu':all_entries})