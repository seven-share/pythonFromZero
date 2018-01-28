'''
request练习
'''

import requests

url_ip='http://httpbin.org/ip'
url_get='http://httpbin.org/get'

res=requests.get(url_ip)
print(res.headers)
print(res.text)

p={'param1':'hello','parms':'world'}
# 参数关键词params，传入字典
r=requests.get(url_get,params=p)
print(r.status_code)
print(r.json())