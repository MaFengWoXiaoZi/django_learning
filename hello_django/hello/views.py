from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse

# Create your views here.

def hello(request, a):
   print(a)
   print(isinstance(request, HttpRequest)) # True
   print(request.path) # return request path
   print(request.get_full_path()) # return entire path
   print(request.method) # GET
   print(request.GET.get('name'))
   print(request.GET.get('key')) # GET method get value
   print(request.POST.get('key')) # POST method get value
   user_list = User.objects.all()
   return render(request, 'table.html', {'user_list': user_list})

def test(request):
	return render(request, 'table.html')

def test2(request, id):
	print(id)
	return render(request, 'table.html')

def test3(request, id, key):
	print(id)
	print('\n')
	print(key)
	return render(request, 'table.html')
