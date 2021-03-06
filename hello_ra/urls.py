"""hello_ra URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
	return render(request, "index.html")

def hello_python(request, a =''):
	return HttpResponse("Hello python " + a)

def sum_two(request, a, b):
	s = int(a) + int(b)
	return HttpResponse("Sum = " + str(s))

urlpatterns = [
    url(r'^$', hello),
	url(r'^python/(?P<a>\w+)', hello_python),
	url(r'^python/', hello_python),
	url(r'^sum/(?P<a>\d+)/(?P<b>\d+)$', sum_two),
    url(r'^admin/', admin.site.urls),

]
