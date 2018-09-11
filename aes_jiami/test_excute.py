#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import time
import hashlib
import audio
from Crypto.Cipher import AES

BS = 16
pad = lambda s: s + (BS - len(bytes(s, 'utf-8')) % BS) * chr(BS - len(bytes(s, 'utf-8')) % BS)

def TuringMD5(secret, ticks, apiKey):
    strs = secret + str(ticks) + apiKey
    m = hashlib.md5()
    m.update(strs.encode("utf-8"))
    aeskey = m.hexdigest()
    return aeskey

# str不是16倍数的补足
def add_to_16(value):
    while len(bytes(value, "UTF-8")) % 16 != 0:
        value = str(value)
        value += ' '
    return value


def TuringAES(aeskey, data_json):
    aes = AES.new(aeskey, AES.MODE_CBC, IV='\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0')
    # aes = AES.new(aeskey, AES.MODE_ECB)
    print('ase', aes)
    data_json_16 = pad(data_json)
    encrypted_datas = str(audio.encodebytes(aes.encrypt(data_json_16)), encoding='utf-8').replace('\n', '')
    return encrypted_datas


url = "http://api.turingos.cn/turingosapi"
apiKey = "17886eeb02c44a7dbcde3a2f8cb09e9f"
secret = "35Bl356M74MWY0I9"
userid = "160084096"
cmd = "你好"
datas = {"appState": {"code": 10000, "appkey": apiKey, "operateState": 0, "paramters": {}},
             "perception": {"audition": {"text": cmd}},
             # -1 聊天， 1 主动交互， 3 开机提示
             "reqType": -1,
             "userInfo": {"userId": userid, "key": apiKey}}
data_json = json.dumps(datas, ensure_ascii=False).replace(' ', '')
ticks = int(time.time() * 1000)
print(ticks)
# MD5
aeskey = TuringMD5(secret, 1528780182484, apiKey)
print("aeskey", aeskey)
# AES
encrypted_a = TuringAES(aeskey, data_json)
print("加密结果", encrypted_a)

aa = {"data": encrypted_a, "key": apiKey, "timestamp": ticks}
print("aa", aa)
hh = {'Content-Type': 'application/json'}
response = requests.post(url, json=aa, headers=hh)
results_json = response.json()
print("请求结果", results_json)
