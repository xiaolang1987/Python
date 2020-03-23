#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import http.client
import urllib.request
import json
import os

"""
喜马拉雅爬虫
"""

download_list = [["刘慈欣_地球大炮", "4364796", "1"],
                 ["刘慈欣_梦之海", "419485", "1"],
                 ["刘慈欣_光荣与梦想", "4261169", "1"],
                 ["刘慈欣_白垩纪往事", "244099", "1"],
                 ["刘慈欣_超新星纪元", "5461987", "2"],
                 ["刘慈欣_魔鬼积木", "4389305", "1"],
                 ["100个著名女人", "23341587", "2"],
                 ["刘慈欣_时间移民", "11639158", "3"],
                 ["影响中国历史的100件大事", "24588883", "4"],
                 ]
"""
["中国历史上的那些女人", "25097608", "4"],
["三十六计的故事", "12369609", "15"],
["重读毛泽东", "11927809", "3"],
["希腊神话故事", "4017569", "4"],
["", "", ""],
["", "", ""],
["", "", ""],
["", "", ""],
["", "", ""]
"""
fail_list = []
for list in download_list:
    foldername = list[0]
    albumId = list[1]
    looptime = list[2]
    path = "D:/00-work/audio/"
    try:
        print(path + foldername)
        os.mkdir(path + foldername)
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
        # conn.request("GET", "/revision/play/album?albumId=" + albumId + "&pageNum=" + str(x) + "&sort=-1&pageSize=30", headers=headers)
        conn.request("GET", "/revision/play/v1/show?id=" + albumId + "&num=" + str(x) + "&sort=0&size=60&ptype=0",
                     headers=headers)
        res = conn.getresponse()
        data = res.read()
        # print(data)

        all_content = json.loads(data.decode("utf-8"))['data']['tracksAudioPlay']
        print("获取的内容%s" % all_content)
        if len(all_content) != 0:
            for i in range(len(all_content)):
                trackName = all_content[i]['trackName']
                trackId = all_content[i]['trackId']
                print("文件名：%s，文件id：%s" % (trackName, trackId))

                # get_url_conn = http.client.HTTPSConnection("www.ximalaya.com")
                try:
                    conn.request("GET", "/revision/play/v1/audio?id=%s&ptype=1" % trackId,
                                 headers=headers)
                    get_url_res = conn.getresponse()
                    get_url_data = get_url_res.read()
                    url = json.loads(get_url_data.decode("utf-8"))['data']['src']
                except:
                    try:
                        conn.request("GET", "/revision/play/v1/audio?id=%s&ptype=1" % trackId,
                                     headers=headers)
                        get_url_res = conn.getresponse()
                        get_url_data = get_url_res.read()
                        url = json.loads(get_url_data.decode("utf-8"))['data']['src']
                    except:
                        url = ""
                        fail_list.append(trackId)
                        print(fail_list)
                print(url)
                print("获得链接，正在下载....")
                try:
                    audio_file = urllib.request.urlopen(url)
                    get_file = audio_file.read()
                    with open(path + foldername + '/' + trackName.replace("|", "") + '.m4a', 'wb') as f:
                        f.write(get_file)
                        print("下载完成...." + '\n')
                except:
                    fail_list.append(trackId)
                    print(fail_list)
