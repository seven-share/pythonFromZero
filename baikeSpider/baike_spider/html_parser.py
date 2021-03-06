'''
获取页面所需要分析的内容
'''
import urllib.parse
from bs4 import BeautifulSoup
import re

class HtmlParser(object):
    def __get_new_urls(self,page_url,soup):
        '''
        获取页面的链接
        '''
        links=soup.find_all('a',href=re.compile(r"/item/.*"))
        new_urls=set()

        for link in links:
            new_url=link['href']
            new_full_url=urllib.parse.urljoin(page_url,new_url)
            new_urls.add(new_full_url)
        return new_urls


    def __get_new_data(self,page_url,soup):
        '''
        获取页面的标题和简介
        '''
        res_data={}
        res_data['url']=page_url
        # <dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        title_node=soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find('h1')
        res_data['title']=title_node.get_text()
        # <div class="lemma-summary" label-module="lemmaSummary">
        summary_node=soup.find('div',class_='lemma-summary')
        res_data['summary']=summary_node.get_text()

        return res_data
    def parse(self,page_url,html_cont):
        '''
        主要执行函数
        '''
        if page_url is None or html_cont is None:
            return
        soup=BeautifulSoup(html_cont,'html.parser')
        new_urls=self.__get_new_urls(page_url,soup)
        new_data=self.__get_new_data(page_url,soup)
        return new_urls,new_data
