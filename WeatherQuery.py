# -*- coding: UTF-8 -*-

import urllib2
import json

# web = urllib2.urlopen('http://www.baidu.com')
# content = web.read()
#
# out = open('baidu.html','w')
# out.write(content)
# out.close()

from city import city

cityName = raw_input('请输入你要查询的城市:\n')
cityCode = city.get(cityName)

if cityCode:
    try:
        url = ('http://www.weather.com.cn/data/cityinfo/%s.html' % cityCode)
        web = urllib2.urlopen(url)
        content = web.read()
        data = json.loads(content)
        result = data['weatherinfo']
        strResult = '%s\n%s --- %s' % (result['city'], result['temp1'], result['temp2'])
        print strResult
    except:
        print '查询失败'
else:
    print '没有找到这个城市'
