import oauth2 as oauth
import httplib2
import time, os, simplejson
import pprint
import yaml

# read skillstack yaml file
yc = yaml.load(open("./skillstack.yaml"))
pprint.pprint(yc)

# Use your API key and secret to instantiate consumer object
consumer = oauth.Consumer(yc['linkedin']['consumer_key'], yc['linkedin']['consumer_secret'])

# Use your developer token and secret to instantiate access token object
access_token = oauth.Token(key=yc['linkedin']['user_token'], secret=yc['linkedin']['user_secret'])

client = oauth.Client(consumer, access_token)

# Make call to LinkedIn to retrieve your own profile
resp,content = client.request(yc['linkedin']['skills'], "GET", "")

# By default, the LinkedIn API responses are in XML format. If you prefer JSON, simply specify the format in your call
#resp,content = client.request("http://api.linkedin.com/v1/people/~?format=json", "GET", "")
#resp,content = client.request("http://api.linkedin.com/v1/companies/1337/updates?event-type=status-update", "GET", "")

pprint.pprint(resp)
pprint.pprint(content)
