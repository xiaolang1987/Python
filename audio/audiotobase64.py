#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import audio

allfile = []
def getallfile(path):
    allfilelist = os.listdir(path)
    for file in allfilelist:
        filepath = os.path.join(path, file)
        # 判断是不是文件夹
        if os.path.isdir(filepath):
            getallfile(filepath)
        allfile.append(filepath)
    return allfile



getallfile("C:\\zhaopeng\\01-items\\01-doc\\02-ASR\\音频文件-80k左右\\")
f_out = open('base64_result.txt', 'w')
for item in allfile:
    print(item)
    cmd = open(item, 'rb')
    dd = str(audio.b64encode(cmd.read()), 'utf-8')
    print(dd)
    # f_out.write(item + '\n')
    f_out.write(dd + '\n')




