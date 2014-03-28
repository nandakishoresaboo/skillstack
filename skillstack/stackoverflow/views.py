# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

def hello_world(request):
  return HttpResponse("Hello World")

def test_stackoverflow(request):
  return render(request,"sindex.html",{})
