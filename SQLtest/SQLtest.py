import codecs
import os,sys
import re

str = '你喜欢什么故事啊，能告诉我吗'
# str = '你喜欢什么动画片'
class Item:
    def __init__(self, line):
        self.content = line
        self.userid = line.split()[11]
        self.tag = str in line.split()[4]

dic = {}

f_in = codecs.open('shijianduan.txt', 'r', 'utf8')
out = codecs.open('out.txt', 'w', 'utf8')

for line in f_in.readlines():
    try:
        item = Item(line.strip())
    except Exception:
        print(line)

    if item.userid in dic.keys():
        out.write(dic.pop(item.userid) + '\n' + item.content + '\n\n')
    if item.tag == True:
        dic[item.userid] = item.content
f_in.close()
out.close()

