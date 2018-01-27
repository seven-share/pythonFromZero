'''
爬取今日头条
内容从js接口中获取
'''
import requests
import json

url='http://www.toutiao.com/api/pc/focus/'
# 找到js接口
web_data=requests.get(url).text
data=json.loads(web_data)
news=data['data']['pc_feed_focus']

for n in news:
    title=n['title']
    img_url = n['image_url']    
    url = n['media_url']    
    print(url,title,img_url)