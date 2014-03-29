# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
import oauth2 as oauth
import httplib2
import time, os, simplejson
import pprint
import yaml
from skillstack import OATH_SETTINGS

def hello_world(request):
  return HttpResponse("Hello World")

def blank_page(request):
  return HttpResponse('')

def test_stackoverflow(request):
  # read skillstack yaml file
   yc = yaml.load(open(OATH_SETTINGS))
   return render(request,"sindex.html",{})
