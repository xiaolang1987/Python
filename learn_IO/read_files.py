#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import audio


# 获取文件列表
def getallfile(path):
    allfile = []
    allfilelist = os.listdir(path)
    for file in allfilelist:
        filepath = os.path.join(path, file)
        # 判断是不是文件夹
        if os.path.isdir(filepath):
            getallfile(filepath)
        allfile.append(filepath)
    return allfile


# 读取多段内容并保存
def read_content(files):
    lines = open(files, "r", encoding="utf-8").readlines()
    fr = open("result.txt", "w", encoding="utf-8")
    start_line = []
    end_line = []
    line_num = 0
    for line in lines:
        if "qwerty" in line:
            start_line.append(line_num)
        if "the end" in line:
            end_line.append(line_num)
        line_num += 1
    print(start_line, end_line)
    for i in range(len(start_line)):
        for j in lines[start_line[i]+1:end_line[i]]:
            fr.write(j)


if "__name__" == "__name__":
    read_content("read.txt")


