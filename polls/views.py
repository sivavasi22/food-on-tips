from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return "Hello, world. You're at the polls index."
def lib(request):
	return "{% load static %}<br> <img src=\"{% static \"myapp/img/alex.jpg\" %}\" alt=\"My image\"/>"
def hello(request):
	return render(request, "hello.html",{})
def hello2(request):
	#text = index(request);
	library = lib(request)
	return HttpResponse("<html><body><h1>Hello</h1>%s</body></html>" % library)

# Create your views here.
