import urllib.request
from bs4 import BeautifulSoup
import json
# import os
# import re

# path = "C:\\zhaopeng\\01-items\\01-AutoTest\\Python\\larnPython\\"
# os.chdir(path)

# id = ['28455189', '28455463', '28456840', '28456841', '28456842']
#
# for id in id:
#     id = str(id)
#     url = 'http://www.ximalaya.com/tracks/' + id + '.json'
#     print(id)
#
#     req = urllib.request.Request(url)
#     req.add_header('User-Agent',
#                    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')
#     response = urllib.request.urlopen(req)
#     result = response.read().decode('utf-8')
#     print(result)
#
#     jsons = json.loads(result)
#     url = jsons['play_path_64']
#     name = jsons['title']
#
#     print(jsons)
#     print(url)
#     print(name)
#
#     # audio_file = urllib.request.urlopen(url)
#     # get_file = audio_file.read()
#     #
#     # with open(name + '.m4a', 'wb') as f:
#     #     f.write(get_file)
#
# print('ok')

fr = open("url.txt", "r", encoding="utf-8")
items = fr.readlines()
i = 1
for item in items:
    print(i)
    name = item.split('\t', 1)[0]
    url = item.split('\t', 1)[1]
    audio_file = urllib.request.urlopen(url)
    get_file = audio_file.read()
    with open('C:\\zhaopeng\\01-items\\01-doc\\三国演义\\' + name + '.m4a', 'wb') as f:
        f.write(get_file)
    i += 1


# for id in id:
#     id = str(id)
#     print(id)
#     url = 'http://www.ximalaya.com/tracks/' + id + '.json'
#
#     req = urllib.request.Request(url)
#     req.add_header('User-Agent',
#                    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')
#     response = urllib.request.urlopen(req)
#     result = response.read().decode('utf-8')
#
#     jsons = json.loads(result)
#     url = jsons['play_path_64']
#     name = jsons['title']
#
#     print(jsons)
#     print(url)
#     print(name)
#
#     audio_file = urllib.request.urlopen(url)
#     get_file = audio_file.read()
#     print(type(audio_file))
#
#     with open(name + '.m4a', 'wb') as f:
#         f.write(get_file)
#
