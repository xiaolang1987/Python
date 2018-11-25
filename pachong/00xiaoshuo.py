#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request
import requests
import json
from bs4 import BeautifulSoup
import os

fw = open('xiaoshuo.txt', 'w', encoding='utf-8')
fr = open('url.txt', 'r', encoding='utf-8')
lines = fr.readlines()
for line in lines:
    line = line.replace('\n', '')
    title = line.split('\t', 1)[1]
    url = line.split('\t', 1)[0]
    print(title)
    print(url)
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
    }

    respone = requests.post(url, headers=header)
    result = respone.content
    jsons = BeautifulSoup(result, "html.parser")
    text = jsons.select('body div')[16]
    text = str(text).replace('<br/><br/>', '').replace(' ', '').replace('<div id="nr1">', '').replace('<br/></div>', '').replace('\n', '').replace('\t', '').replace('\r', '').replace('</div>', '')
    print(text)
    # fw.write(title + '\n')
    fw.write(str(jsons) + '\n')
    fw.flush()
fw.close()

# url = "http://m.69wx.la/book/10/10029/2573337.html"
# header = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
# }
#
# respone = requests.post(url, headers=header)
# result = respone.content
# jsons = BeautifulSoup(result, "html.parser")
# bodys = jsons.select('div')
# # jsons = BeautifulSoup(bodys, "html.parser")
# # text = jsons.select('div')
# # text = str(text).replace('<br/><br/>', '').replace(' ', '').replace('<div id="nr1">', '').replace('<br/></div>',
# #                                                                                                   '').replace('\n',
# #                                                                                                               '').replace(
# #     '\t', '').replace('\r', '').replace('</div>', '')
# print(bodys)
