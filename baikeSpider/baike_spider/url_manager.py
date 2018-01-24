'''
url管理器
'''
class UrlManager(object):

    def __init__(self):
        '''
        定义两个url列表，new代表为爬取，old代表爬取完成
        '''
        self.new_urls=set()
        self.old_urls=set()
        
    def add_new_url(self,url):
        '''
        判断是否存在并添加url
        '''
        if url==None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self,urls):
        '''
        添加url
        '''
        if urls==None or len(urls)==0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        '''
        判断是否还有为爬取的url
        '''
        return len(self.new_urls)!=0

    def get_new_url(self):
        '''
        从new_urls中获取一个url
        '''
        new_url=self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
