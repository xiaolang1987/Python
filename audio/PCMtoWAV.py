#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import wave

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

audio_path = 'C:\\zhaopeng\\01-items\\01-doc\\02-ASR\\音频文件-80k左右1\\'
# audio_path = '/repo/public/public/50-JenkinsTestFile/pcm/'
getallfile(audio_path)
for item in allfile:
    print(item)
    file_name = item.replace(audio_path, '').replace('.pcm', '')
    print(file_name)
    files = open(item, 'rb')
    str_data = files.read()
    wave_out = wave.open('C:\\zhaopeng\\01-items\\01-doc\\02-ASR\\audio2\\' + file_name + '.wav', 'wb')
    wave_out.setnchannels(1)
    wave_out.setsampwidth(2)
    wave_out.setframerate(16000)
    wave_out.writeframes(str_data)
