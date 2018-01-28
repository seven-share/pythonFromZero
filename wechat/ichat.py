'''
微信itchat库尝试
'''

import itchat
from echarts import Echart,Legend,Pie

itchat.auto_login(hotReload=True)

friends = itchat.get_friends()

male = female = other = 0

for person in friends[1:]:
    sex=person['Sex']
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other += 1

total = len(friends[1:])
male_percent=round(male/total*100,2)
print(type(male_percent))
female_percent=round(female/total*100,2)
othor_percent=100-male_percent-female_percent

print("一共好友数：{0}".format(total))
print("男性好友：{0},占比：{1}%".format(male,male_percent))
print("女性好友：{0},占比：{1}%".format(female,female_percent))


# 画饼状图并未成功，python-echart文档正在做，查询未果
from echarts import Echart, Legend, Pie

chart = Echart(u'{0}的微信好友性别比例'.format(friends[0]['NickName']), 'from WeChat')

chart.use(Pie('wechat',data=[
    {'name:男性占比{1}%, value:{0}'.format(male,male_percent)},
    {'name:女性占比占比{1}%, value:{0}'.format(female,female_percent)},
    {'name:其他占比占比{1}%, value:{0}'.format(other,othor_percent)}
],radius=['50%','70%']))

chart.use(Legend(data=["male", "female", "other"]))
del chart.json["xAxis"]
del chart.json["yAxis"]
chart.plot()
