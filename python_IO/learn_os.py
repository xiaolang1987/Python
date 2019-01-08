#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os

"""删除文件"""
# 如果目标文件存在则删除，如果不存则在跳过
# try:
#     os.remove("C:\\zhaopeng\\test\\111.txt")
#     print("删除成功")
# except:
#     print("没有该文件")
#     pass


"""创建文件夹"""
# os.path.exists(path) 判断文件夹是否存在返回结果True、False
path = "C:\\zhaopeng\\test\\1\\2\\"
if os.path.exists(path) is False:
    os.makedirs(path)  # 可以创建多级目录
    # os.mkdir(path)  # 只能创建最后一级文件夹

