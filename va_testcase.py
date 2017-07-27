import unittest
import time
import sys
from .va_api import APIManager

class TestClass(unittest.TestCase):
#   api = APIManager(va_url='https://127.0.0.1/api',token='daeebbeddbc0471d8d7f5ae2e7b5429c', verify=False)
    api = APIManager(va_url='https://127.0.0.1:443', va_user=sys.argv[1], va_pass=sys.argv[2], verify=False)
#    def setUp(self):
#	self.api = APIManager(va_url='https://127.0.0.1/api',token='daeebbeddbc0471d8d7f5ae2e7b5429c', verify=False)
#	self.api = APIManager(va_url='htpps://127.0.0.1/api', va_user=sys.argv[1], va_pass=sys.argv[2], verify=False)
#	a = self.api.api_call('/login', method='post', data={"username": sys.argv[1], "password": sys.argv[2]})
#	data = a['data']
#	token_value = data['token']
#	self.api = APIManager(va_url='https://127.0.0.1/api',token=token_value, verify=False)
#    def test_hosts(self):
#        #api = APIManager(va_url='https://127.0.0.1/api',token='la882c9e22c2462d95dcadb8a127bb8d', verify = False)
#	a = self.api.api_call('/hosts', method='get', data = {})
	#print a['success']
#	self.assertTrue(a['success'])
    def test_login(self):
	a = self.api.api_call('/login', method='post', data={"username" : sys.argv[1], "password" : sys.argv[2]})
	data = a['data']
	token = data['token']
 	print (token)
	self.assertTrue(a['success'])
    de 
	f test_panels_ts_data(self):
        a = self.api.api_call('/panels/ts_data', method='get', data = {})
        #print a['success']
        self.assertTrue(a['success'])
#    def test_triggers(self):
#	a = self.api.api_call('/triggers', method='get', data= {})
#	self.assertTrue(a['success'])
#    def test_hosts_reset(self):
#	a = self.api.api_call('/hosts/reset', method='get', data={})
#	print a['success'] 
#       self.assertTrue(a['success'])
    def test_states_stores(self):
	a = self.api.api_call('/states', method='get', data={})
	self.assertTrue(a['success'])
    def test_list_panels(self):
	a = self.api.api_call('/panels', method='get', data={})
	self.assertTrue(a['success'])
    def test_list_hosts(self):
	a = self.api.api_call('/hosts/info', method='post', data={})
        self.assertTrue(a['success'])
    def test_list_vpn_users(self):
	a = self.api.api_call('/apps/vpn_users', method='get', data={})
	self.assertTrue(a['success'])
    def test_get_vpn_status(self):
	a = self.api.api_call('/apps/vpn_status', method='get', data={})
	print(a['success'])
        self.assertTrue(a['success'])
    def test_add_host(self):
	hosts =  self.api.api_call('/hosts/info', method='post', data={})
	time.sleep(5)
	cekor1 = self.api.api_call('/hosts/new/validate_fields', method='post', data={"driver_id" : "openstack", "field_values" : {}, "step_index" : -1})
        cekor2 = self.api.api_call('/hosts/new/validate_fields', method='post', data={"driver_id" : "openstack", "field_values" : {"hostname" : "va-os", "username" : "admin", "tenant" : "admin", "host_ip" : "192.168.80.16:5000", "region" : "RegionOne", "password" : "zilxii4g2j"}, "step_index" : 0})
	cekor3 = self.api.api_call('/hosts/new/validate_fields', method='post', data={"driver_id" : "openstack", "field_values" : {"sec_group" : "default|26811978-5201-41e5-8860-f71607928114", "network" : "public|9bd9a1c4-c46d-4976-b5a8-41c6c670bef2"}, "step_index" : 1})
	cekor4 = self.api.api_call('/hosts/new/validate_fields', method='post', data={"driver_id" : "openstack", "field_values" : {"size" : "va-medium", "image" : "debian-jessie"}, "step_index" : 2})
	time.sleep(5)
	new_hosts = self.api.api_call('/hosts/info', method='post', data={})
	diff_hosts = [x for x in new_hosts if x not in hosts]
	#print(diff_hosts)
	print(len(hosts['data']))
	print(len(new_hosts['data']))
	self.assertNotEqual(len(hosts['data']), len(new_hosts['data']))
    def test_delete_host(self):
	hosts = self.api.api_call('/hosts/info', method='post', data={})
	time.sleep(5)
	a = self.api.api_call('/hosts/delete', method='post', data={"hostname": "va-os"})
	time.sleep(5)
	new_hosts = self.api.api_call('/hosts/info', method='post', data={})
	time.sleep(5)
	print(len(hosts['data']))
        print(len(new_hosts['data']))
	self.assertNotEqual(len(hosts['data']), len(new_hosts['data']))

if __name__ == '__main__':
    print(len(sys.argv))
    print(sys.argv)
    suite = unittest.TestLoader().loadTestsFromTestCase(TestClass)
    unittest.TextTestRunner(verbosity=5).run(suite)
