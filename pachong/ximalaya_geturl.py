#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request

url = "https://www.ximalaya.com/revision/play/album?albumId=3289361&pageNum=1&sort=-1&pageSize=30"
responce = urllib.request.urlopen(url)
result = responce.read().decode('utf-8')
print(result)
