#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://www.bilibili.com/video/av17118368/?p=103

import time
from ws4py.client.threadedclient import WebSocketClient
import websocket
from websocket import ABNF
import json
import _thread
import ssl


def on_open(ws):
    def run(*args):
        content = {
            'key': '9646E24E7386419CA2D37C1F6B9F156D',
            'version': '2.0',
            'device_id': '8AB135F3A9E344B3B84EBF7095848EE6',
            'device_type_id': 'D4AF278E39F64BD1A47AB889A532AE25',
            'service': 'speech',
            'secret': '20B83529FBB44ADC9AAF5B808CC26930',
            'voiceFile': item,
            'text': '',
            'vt': '',
            'vend_timeout': '500',
            'codec': 'pcm',
            'language': 'zh',
            'vad_mode': 'cloud',
            'no_nlp': 'false',
            'no_intermediate_asr': 'false',
            'stack': '',
            'voice_power': '100',
            'vpr_start': '0',
            'vpr_length': '9600',
            'skill': ''
        }
        print(content)
        ws.send(json.dumps(content))
        step = 3200
        with open(item, 'rb') as f:
            print(item)
            while True:
                data = f.read(step)
                if data:
                    ws.send(data, ABNF.OPCODE_BINARY)
                    if len(data) < step:
                        break
                    time.sleep(0.1)
        ws.send('', ABNF.OPCODE_BINARY)
        print("进程结束...")
    _thread.start_new_thread(run, ())


def on_message(ws, message):
    message_json = json.loads(message)
    test = message_json['result']['rec'].replace(' ', '')
    print(test)
    ws.close()

item = 'Z:\\50-JenkinsTestFile\\zhiwa_pcm\\220506.pcm'
url = "wss://apigwws.open.rokid.com/api"
ws = websocket.WebSocketApp(url, on_message=on_message)
ws.on_open = on_open
ws.run_forever(sslopt={})





# class DummyClient(WebSocketClient):
#     def opened(self):
#         self.send("{'key':'9646E24E7386419CA2D37C1F6B9F156D','version':'2.0','device_id':'8AB135F3A9E344B3B84EBF7095848EE6','device_type_id':'D4AF278E39F64BD1A47AB889A532AE25','service':'speech','secret':'20B83529FBB44ADC9AAF5B808CC26930','voiceFile':'Z:\\50-JenkinsTestFile\\temp\\temp\\10万个为什么是谁写的.pcm','text':'','vt':'','vend_timeout':'500','codec':'pcm','language':'zh','vad_mode':'cloud','no_nlp':'false','no_intermediate_asr':'false','stack':'','voice_power':'100','vpr_start':'0','vpr_length':'9600','skill':''}")
#
#     def close(self, code=1000, reason=None):
#         print("Close down", code, reason)
#
#     def received_message(self, m):
#         print("recv", m)
#
# ws = DummyClient('wss://apigwws.open.rokid.com/api', protocols=['chat'])
# ws.connect()
# ws.send("test")
# ws.run()
# ws.close()


