'''
request下载图片
'''
import requests

def download():
    url="http://yzhtml01.book118.com/2016/11/27/19/45710191/1.files/file0001.jpeg"
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
    res=requests.get(url,headers=headers)
    with open('demo.jpg','wb') as f:
        f.write(res.content)

download()