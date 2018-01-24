'''
爬取百度百科python页面，将页面链接爬取出来，继续爬取
保存每次爬取的页面的标题和简介
最后用html页面展示
'''
from baike_spider import url_manager,html_downloader,html_parser,html_outputer

class SpiderMain(object):
    def __init__(self):
        '''
        初始化各个类
        '''
        self.urls=url_manager.UrlManager()
        self.downloader=html_downloader.HtmlDownloader()
        self.parser=html_parser.HtmlParser()
        self.outputer=html_outputer.HtmlOutputer()
    
    def craw(self,root_url):
        '''
        主要执行函数
        '''
        count=1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url=self.urls.get_new_url()
                print('craw '+str(count)+' : '+new_url)
                # print('craw %d : %s' % (count, new_url))

                html_cont=self.downloader.download(new_url)
                new_urls,new_data=self.parser.parse(new_url,html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                # 此为获取内容的条数，由于测试，仅为2条，可以修改数字爬取更多
                if count==2:
                    break
                count+=1

            except:
                print('craw fail')
            
        self.outputer.output_html()

# 网址可能会有变化，可随机更改
root_url='https://baike.baidu.com/item/Python/407313'
obj_spider=SpiderMain()
obj_spider.craw(root_url)