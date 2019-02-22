#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import http.client
import urllib.request
import json
import os

"""
喜马拉雅爬虫
"""

download_list = [["金瓶梅-评书", "18710076", "4"]]
#   ,["", "", ""]
for list in download_list:
    foldername = list[0]
    albumId = list[1]
    looptime = list[2]
    try:
        os.mkdir("C:\\zhaopeng\\01-items\\01-doc\\" + foldername)
    except:
        pass
    for x in range(int(looptime)):
        x = x + 1
        print(x)
        conn = http.client.HTTPSConnection("www.ximalaya.com")
        headers = {
            'cache-control': "no-cache",
            'postman-token': "13aa2553-fcfd-2212-2d11-1f9094ca1d20"
            }
        conn.request("GET", "/revision/play/album?albumId=" + albumId + "&pageNum=" + str(x) + "&sort=-1&pageSize=30", headers=headers)
        res = conn.getresponse()
        data = res.read()
        print(data)

        all_content = json.loads(data.decode("utf-8"))['data']['tracksAudioPlay']
        for i in range(len(all_content)):
            name = all_content[i]['trackName'].split('[', 1)[0]
            url = all_content[i]['src']
            print(name + '\t' + url)
            print("获得链接，正在下载....")
            audio_file = urllib.request.urlopen(url)
            get_file = audio_file.read()
            with open('C:\\zhaopeng\\01-items\\01-doc\\' + foldername + '\\' + name + '.m4a', 'wb') as f:
                f.write(get_file)
                print("下载完成...." + '\n')
