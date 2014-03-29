# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
import oauth2 as oauth
import urlparse
import yaml
import pprint
import httplib2
import time, os, simplejson

# read skillstack yaml file
yc = yaml.load(open("../skillstack/skillstack.yaml"))

return render(request,"sindex.html",{})

consumer_key = ycfg['linkedin']['consumer_key']
consumer_secret = ycfg['linkedin']['consumer_secret']

request_token_url = ycfg['linkedin']['request_token_url']
access_token_url = ycfg['linkedin']['access_token_url']

consumer = oauth.Consumer(consumer_key, consumer_secret)
client = oauth.Client(consumer)

resp, content = client.request(request_token_url, "POST")
if resp['status'] != '200':
  raise Exception("Invalid response %s." % resp['status'])

request_token = dict(urlparse.parse_qsl(content))
pprint.pprint("Request Token:\n\toauth_token: %s\n\toauth_token_secret: %s" %(request_token['oauth_token'], request_token['oauth_token_secret']))

resp, content = client.request(access_token_url, "POST")
access_token = dict(urlparse.parse_qsl(content))

#token = oauth.Token(request_token['oauth_token'], request_token['oauth_token_secret'])
#client = oauth.Client(consumer, token)

def skills():
  response = client.request(ycfg['linkedin']['skills'], "GET", '')
  return response

def user():
  pass

def network():
  response = client.request(ycfg['linkedin']['network'], "GET", '')
  return response

