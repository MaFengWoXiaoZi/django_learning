from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

def hello(request, a):
   print(a)
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
