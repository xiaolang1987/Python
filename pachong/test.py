#!/usr/bin/env python3
# -*- coding: utf-8 -*-

fr = open('url.txt', 'r', encoding='utf-8')
fw = open('result1.txt', 'w', encoding='utf-8')

# lines = fr.readlines()
# for line in lines:
#     if '<div id="nr1">' in line:
#         line = line.replace('<div id="nr1">', '').replace('<br/>', '')
#         line = line.replace(' ', '')
#         line = line.replace('</div>', '')
#         line = line.replace('</body></html>', '')
#         line = line.replace('**丝', '')
#         line = line.replace('（）', '')
#         fw.write(line + '\n')
# fw.close()
lines = fr.readlines()
for line in lines:
    item = line.split('\t', 1)[1]
    fw.write(item + '\n')
fw.close()
