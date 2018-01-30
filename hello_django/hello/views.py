from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.template import loader

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

   # t = loader.get_template('table.html')
   # c = {'user_list': user_list}
   # return HttpResponse(t.render(c, request),
   #                     content_type='text/html ')
   print(user_list.query) # print SQL codes
   return render(request, 'table.html', {'user_list': user_list})

   # response = HttpResponse('Here \'s the text of the Web page')
   # return response

   # return render_to_response('table.html', {'user_list': user_list})

   # print(locals())
   # return render_to_response('table.html', locals())

   # return redirect('/test2/22/')  # redirect to one page

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
