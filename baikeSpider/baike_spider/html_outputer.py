'''
将获取内容填充到网页
'''
class HtmlOutputer(object):
    def __init__(self):
        self.datas=[]
    def collect_data(self,data):
        '''
        将所需数据存取变量
        '''
        if data is None:
            return
        self.datas.append(data)
    def output_html(self):
        '''
        遍历填入网页
        '''

        # 此处注意页面的编码encoding，否则有可能乱码
        fout=open('output.html','w',encoding='utf-8')
        fout.write('<html>')
        fout.write('<body>')
        fout.write('<table>')
        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td>%s</td>'%data['url'])
            fout.write('<td>%s</td>'%data['title'])
            fout.write('<td>%s</td>'%data['summary'])
            fout.write('</tr>')
        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')
        fout.close()