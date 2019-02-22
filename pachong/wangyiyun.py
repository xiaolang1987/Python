#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import requests


responce = requests.post("https://music.163.com/#/song?id=35847388")
result = str(responce.content, "utf-8")

print(result)
