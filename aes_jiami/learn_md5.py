#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
import time
import sys

# secret = 'M1Jd39JP5G1pNp0Y'
# key = 'f5a4241a7ccc44b090b80a6b5c0c0f51'
# timess = '1523855337185'
#
#
# ticks = int(time.time() * 1000)
# print(ticks)
# strs = secret+timess+key
# print(strs)
# m = hashlib.md5()
# m.update(strs.encode("utf-8"))
# print(m.hexdigest())

appID = 'HR-PROD-ASR000'
deviceID = '0000000000000010'
Secret = '69d6f0e4-9696-4385-9c75-08cbeaa1225a'
# timestamp = 915148800

ticks = int(time.time())
print(ticks)
strs = appID + Secret + deviceID + str(ticks)
print(strs)
m = hashlib.md5()
m.update(strs.encode("utf-8"))
print(m.hexdigest())
