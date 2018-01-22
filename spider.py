'''
爬取熊猫tv主播LOL主播名字，观看人数
并根据观看人数进行排序
'''

from urllib import request
import re

class Spider():
    url='https://www.panda.tv/cate/lol'

    root_pattern='<div class="video-info">([\s\S]*?)</div>'
    name_pattern='</i>([\s\S]*?)</span>'
    number_pattern='<span class="video-number">([\s\S]*?)</span>'

    def __fetch_content(self):
        '''
        使用request爬去网页全部内容
        '''
        r=request.urlopen(Spider.url)
        htmls=r.read()
        htmls=str(htmls,encoding='utf-8')
        return htmls
        
    def __analysis(self,htmls):
        '''
        使用正则表达式将主播名字和观看人数整体获取下来，存入anchors
        '''
        root_html=re.findall(Spider.root_pattern,htmls)

        anchors=[]
        for html in root_html:
            name=re.findall(Spider.name_pattern,html)
            number=re.findall(Spider.number_pattern,html)
            anchor={'name':name,'number':number}
            anchors.append(anchor)
        
        return anchors
    def __refine(self,anchors):
        '''
        将获取来的数据进行整理，将换行，空格都去掉
        '''

        # 注意去除空格和换行函数
        l=lambda anchor:{
            'name':anchor['name'][0].strip(),
            'number':anchor['number'][0]
            }
        m=map(l,anchors)

        return list(m)
    def __sort(self,anchors):
        '''
        根据观看人数进行排序
        '''
        anchors=sorted(anchors,key=self.__sort_seed,reverse=True)
        
        return anchors
    def __sort_seed(self,anchor):
        '''
        将观看人数数字，作为key返回
        '''
        r=re.findall('\d*',anchor['number'])
        number=float(r[0])

        if '万' in anchor['number']:
            number=number*10000
        
        return number
        
    def __show(self,anchors):
        '''
        将最终结果输出在终端
        '''
        for rank in range(0,len(anchors)):
            print('Rank '+str(rank+1)+'：'+anchors[rank]['name']+'------'+anchors[rank]['number'])
    def go(self):
        '''
        主要执行函数
        '''
        htmls=self.__fetch_content()
        anchors=self.__analysis(htmls)
        anchors=self.__refine(anchors)
        anchors=self.__sort(anchors)
        self.__show(anchors)


spider=Spider()
spider.go()