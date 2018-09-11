#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request
import json
import os


url = 'http://music.163.com/song?id=212168'

req = urllib.request.Request(url)
req.add_header('User-Agent',
               'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')
response = urllib.request.urlopen(req)
result = response.read().decode('utf-8')

print(result)

# jsons = json.loads(result)
# url = jsons['play_path_64']
# name = jsons['title']
