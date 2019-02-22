#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pyhanlp import *


text = "乾隆"
pinyin_list = HanLP.convertToPinyinList(text)
# for pinyin in pinyin_list:
#     print("%s," % pinyin.getPinyinWithoutTone(), end=" ")
print(type(pinyin_list))
for pinyin in pinyin_list:
    print(pinyin)
