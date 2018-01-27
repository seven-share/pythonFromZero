'''
爬取腾讯新闻
'''

import requests
from bs4 import BeautifulSoup

url="http://news.qq.com/"
html=requests.get(url).text
soup=BeautifulSoup(html,'lxml')
news_titles=soup.select("div.text > em.f14 > a.linkto")
# print(news_titles)
# print(news_titles[0].get_text())
# print(news_titles[0].['href'])
for n in news_titles:
    title = n.get_text()
    link=n['href']
    data={
        '标题':title,
        '链接':link
    }
    print(data)