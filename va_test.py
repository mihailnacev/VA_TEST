from va_api import APIManager
import unittest
import ssl

#TODO remove this and work with actual certs. Or maybe have an option. 
#ssl._create_default_https_context = ssl._create_unverified_context
 
#api = APIManager(va_url = 'https://127.0.0.1/api', token = '1a882c9e22c2462d95dcadb8a127bb8d', verify = False)
api = APIManager(va_url = 'https://127.0.0.1', va_user='admin', va_pass='admin', verify = False)

a = api.api_call('/login', method='post', data = {"username":"admin", "password": "admin"})
print a
a = api.api_call('/hosts/info', method = 'post', data = {})
print a
#a = api.api_call('/apps/get_actions', method= 'get', data={})
#print a
a = api.api_call('/states', method='get', data={})
print a
#a = api.api_call('/apps/vpn_status', method='get', data={})
#print a


