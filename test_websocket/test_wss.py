#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://www.bilibili.com/video/av17118368/?p=103

import time
from ws4py.client.threadedclient import WebSocketClient

class DummyClient(WebSocketClient):
    def opened(self):
        self.send("{'key':'9646E24E7386419CA2D37C1F6B9F156D','version':'2.0','device_id':'8AB135F3A9E344B3B84EBF7095848EE6','device_type_id':'D4AF278E39F64BD1A47AB889A532AE25','service':'speech','secret':'20B83529FBB44ADC9AAF5B808CC26930','voiceFile':'Z:\\50-JenkinsTestFile\\temp\\temp\\10万个为什么是谁写的.pcm','text':'','vt':'','vend_timeout':'500','codec':'pcm','language':'zh','vad_mode':'cloud','no_nlp':'false','no_intermediate_asr':'false','stack':'','voice_power':'100','vpr_start':'0','vpr_length':'9600','skill':''}")

    def close(self, code=1000, reason=None):
        print("Close down", code, reason)

    def received_message(self, m):
        print("recv", m)

ws = DummyClient('wss://apigwws.open.rokid.com/api', protocols=['chat'])
ws.connect()
ws.send("test")
ws.run()
ws.close()


