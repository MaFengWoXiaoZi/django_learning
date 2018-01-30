from django.core.urlresolvers import reverse
"""hello_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from hello import views

staticmethod
urlpatterns = [
    url(r'^hello/$', views.hello, {'a': '123'}),
	url(r'^test/\d{2}/$', 'hello.views.test'),
	url(r'^test2/(?P<id>\d{2})/$', 'hello.views.test2'),
	url(r'^test3/(?P<id>\d{2})/(?P<key>\w+)/$', 'hello.views.test3'),
]

#urlpatterns = [
#	url(r'^hello/$', 'hello.views.hello', {'a': '123'})
#]

# The way is not recommended 

#from django.conf.urls import patterns
#from hello import views
#
#urlpatterns = patterns('',
#		(r'^hello/$', views.hello),
#)
