import oauth2 as oauth
import httplib2
import time, os, simplejson
import pprint

# Fill the keys and secrets you retrieved after registering your app
consumer_key = 'k5dropmvdua8'
consumer_secret = '28lEolfpDG2Q0C7w'
user_token = '148ddc0c-6886-48fa-8333-0381a2ea2e82'
user_secret = 'eb11a1e8-25b2-4810-ab48-f7d255b9574f'

# Use your API key and secret to instantiate consumer object
consumer = oauth.Consumer(consumer_key, consumer_secret)

# Use your developer token and secret to instantiate access token object
access_token = oauth.Token(
            key=user_token,
            secret=user_secret)

client = oauth.Client(consumer, access_token)

# Make call to LinkedIn to retrieve your own profile
resp,content = client.request("http://api.linkedin.com/v1/people/~:(skills)", "GET", "")

# By default, the LinkedIn API responses are in XML format. If you prefer JSON, simply specify the format in your call
#resp,content = client.request("http://api.linkedin.com/v1/people/~?format=json", "GET", "")
#resp,content = client.request("http://api.linkedin.com/v1/companies/1337/updates?event-type=status-update", "GET", "")

pprint.pprint(resp)
pprint.pprint(content)