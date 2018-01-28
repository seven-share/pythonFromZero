'''
使用urllib和requests
'''

import urllib
import requests

url_ip='http://httpbin.org/ip'
url_get='http://httpbin.org/get'

def use_simple_urllib():
    res=urllib.request.urlopen(url_ip)
    print(res.readlines())
def use_params_urllib():
    params=urllib.parse.urlencode({'param1':'hello','parms':'world'})
    print(params)
    r=urllib.request.urlopen('?'.join([url_get, '%s']) %params)
    # print(r.info())
    # print(r.readlines())
    for s in r.readlines():
        print(s.strip())
use_simple_urllib()
use_params_urllib()