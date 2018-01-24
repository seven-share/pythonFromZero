'''
下载页面内容并返回
'''
from urllib import request

class HtmlDownloader(object):
    '''
    下载网页内容
    '''
    def download(self,url):
        if url is None:
            return None
        r=request.urlopen(url)
        if r.getcode()!=200:
            return None
        r=r.read()
        return r