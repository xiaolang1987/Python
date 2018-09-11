#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import numpy as np


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


audio_path = "/repo/public/public/50-JenkinsTestFile/zhiwa_wav/"
pcm_path = "/repo/public/public/50-JenkinsTestFile/zhiwa_pcm/"
getallfile(audio_path)

for item in allfile:
    print(item)
    file_name = item.replace(audio_path, '').replace('.wav', '')
    print(file_name)
    f = open(item, "rb")
    f.seek(0)
    f.read(44)
    data = np.fromfile(f, dtype=np.int16)
    data.tofile(pcm_path + file_name + ".pcm")



