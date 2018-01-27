'''
爬取智联招聘
多线程执行（难）

'''

import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool

def get_zhaopin(page):
    url='http://sou.zhaopin.com/jobs/searchresult.ashx?jl=全国&kw=python&p={0}&kt=3'.format(page)
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    print("这是第{0}页".format(page))
    wb_data=requests.get(url,headers=headers).content
    soup=BeautifulSoup(wb_data,'lxml')

    # 计算一共有多少页
    # print(soup)
    # job_one_page=soup.select('table.newlist')
    # job_count_one_page=len(job_one_page)-1
    # print(job_count_one_page)
    # job_all=soup.select('div.seach_yx > span.search_yx_tj > em')[0].get_text()
    # print(job_all)
    # pages=int(job_all)//job_count_one_page
    # print(pages)


    job_name=soup.select('table.newlist > tr > td.zwmc > div > a')
    salarys = soup.select("table.newlist > tr > td.zwyx")
    locations = soup.select("table.newlist > tr > td.gzdd")
    times = soup.select("table.newlist > tr > td.gxsj > span")

    for name, salary, location, time in zip(job_name, salarys, locations, times):
        data = {
            'name': name.get_text(),
            'salary': salary.get_text(),
            'location': location.get_text(),
            'time': time.get_text(),
        }
        print(data)
for i in range(1,3):
    get_zhaopin(i)

# 多线程执行
# pool = Pool(processes=2)
# pool.map_async(get_zhaopin,[1])
# pool.close()
# pool.join()