#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pydub import AudioSegment
import os
import re


# 循环目录下所有文件
for each in os.listdir('.'):
    filename = re.findall(r"(.*?)\.mp3", each) # 取出.mp3后缀的文件名
    if filename:
        filename[0] += '.mp3'
        mp3 = AudioSegment.from_mp3(filename[0]) # 打开mp3文件
        mp3[17*1000+500:].export(filename[0], format="mp3") # 切割前17.5秒并覆盖保存
