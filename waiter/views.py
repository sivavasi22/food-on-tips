from django.shortcuts import render
from . models import Waiter
from django.shortcuts import redirect
# Create your views here.
def waiter(request):
	waiter_tasks = Waiter.objects.all()
	return render(request,'waiterview.html',{'waiter':waiter_tasks})

def update_waiter_task(request,task_id):
	wait = Waiter.objects.filter(id=task_id)
	for w in wait:
		if w.status == 'N':
			Waiter.objects.filter(id=task_id).update(status='A')
	return redirect('/waiter/')