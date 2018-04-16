#!python
#log/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from addfood.models import Employee
from django.shortcuts import redirect
from .forms import LoginForm
# Create your views here.
# this login required decorator is to not allow to any
# view without authenticating
@login_required(login_url="login/")
def home(request):
	if request.method == 'POST':
		ID = request.POST.get('username')
		passw = request.POST.get('password')
		form = LoginForm(request.POST)
		e = Employee.objects.filter(emp_id=ID).filter(emp_pass=passw)
		if len(e) == 1:
			for emp in e:
				if emp.emp_type=='C':
					return redirect("/chef")
				if emp.emp_type=='W':
					return redirect("/waiter")
		else:
			return render(request,"login.html",{'form':form})
	else:	
		form = LoginForm()
		return render(request,"login.html",{'form':form})
	'''return HttpResponse("<h1>welcome to home page</h1>")'''

def detail(request):
	return render(request,"detail.html")

def aboutus(request):
	return render(request,"aboutus.html")