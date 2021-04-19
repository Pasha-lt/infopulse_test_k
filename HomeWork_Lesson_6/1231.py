import requests
import http.client
import pprint

t = requests.get('http://httpbin.org/get')
import pprint

pprint.pprint(t.json())



