#!/usr/bin/env python
# -*- coding: utf-8 -*-


import urllib.request
import json
from bs4 import BeautifulSoup
import os

fr = open('url.txt', 'r', encoding='utf-8')
lines = fr.readlines()
for line in lines:
    url = line.split('\t', 1)[0].replace('\t', '')
    tital = line.split('\t', 1)[1].replace('\n', '')
    print('\n\n' + 'url=' + url + 'tital=' + tital)
    url1 = 'http://99.hhxxee.com' + url
    print('url1:' + url1)
    req = urllib.request.Request(url1)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')
    response = urllib.request.urlopen(req)
    result = response.read()
    jsons = BeautifulSoup(result, "html.parser")
    a = jsons.select('script')[0].get_text()
    b = a.replace('var sFiles="', '').replace('";var sPath="1";', '')
    countb = b.count('|') + 1
    print('all = ' + b)
    print(countb)
    for i in range(countb):
        print(i)
        c = b.split('|', int(countb))[i]
        print(c)
        down_url = 'http://98.94201314.net/dm01/' + c
        print('dwon_url:', down_url)
        img = urllib.request.urlopen(down_url)
        img = img.read()
        with open('E:\\audio\\chugui\\' + tital + str(i + 1).zfill(3) + '.jpg', 'wb') as down_img:
            down_img.write(img)
        i += 1

