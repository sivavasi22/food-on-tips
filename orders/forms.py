from django import forms
from orders.models import Orders
from menu.models import FoodItem
from django.forms import formset_factory,ModelForm
# import itertools
class Order(forms.Form):
	"""docstring for ClassName"""
	# qty = forms.IntegerField()
	# food_item = forms.BooleanField()
	
	#c = ()
	
	all_entries = FoodItem.objects.all()
# 		#c= itertools.chain((item.id,item.name), c)
	food_choices = forms.ModelMultipleChoiceField(queryset = all_entries,widget=forms.CheckboxSelectMultiple)