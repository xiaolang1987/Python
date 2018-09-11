#!/usr/bin/env python
# -*- coding: utf-8 -*-


#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request
import json
from bs4 import BeautifulSoup
import os

fw = open('xiaoshuo.txt', 'w', encoding='utf-8')
fr = open('url.txt', 'r', encoding='utf-8')


lines = fr.readlines()
for line in lines:
    url = line.split('\t', 1)[0]
    tital = line.split('\t', 1)[1]
    print(url)
    print(url.split('.', 1)[0])
    print(tital)

    url1 = 'http://tianyibook.la/book/' + url
    print("url1:", url1)
    req = urllib.request.Request(url1)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')
    response = urllib.request.urlopen(req)
    result = response.read()
    jsons = BeautifulSoup(result, "html.parser")
    a = jsons.select('body div')[10].get_text()
    # print("a:", a)

    # 第二页
    url2 = 'http://tianyibook.la/book/' + url.split('.', 1)[0] + '_2.html'
    print("url2:", url2)
    req2 = urllib.request.Request(url2)
    req2.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')
    response2 = urllib.request.urlopen(req2)
    result2 = response2.read()
    jsons2 = BeautifulSoup(result2, "html.parser")
    b = jsons2.select('body div')[10].get_text()
    # print("b:", b)
    c = a + b
    c = c.replace('一秒记住【天翼文学 tianyibook.la】，更新快，无弹窗，免费读！！', '')
    c = c.replace('-->>本章未完，点击下一页继续阅读', '')
    # c = c.replace('\n', '')
    fw.write(tital + '\n')
    fw.write(str(c).replace('        ', '').replace('\n', '') + '\n\n')
    fw.flush()
fw.close()

# # 拿地址
# for i in range(24):
#     i = i + 1
#     print(i)
#     url1 = 'http://m.mengzeda.cn/5/5738_' + str(i) + '/'
#     req = urllib.request.Request(url1)
#     req.add_header('User-Agent',
#                    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')
#
#     response = urllib.request.urlopen(req)
#     result = response.read()
#     jsons = BeautifulSoup(result, "html.parser")
#     a = jsons.select('body ul')[0].get_text
#     print(a)
#     fw.write(str(a))
#     fw.flush()
# fw.close()


