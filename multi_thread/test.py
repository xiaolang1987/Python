#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
import time

thread_count = 11


class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("开始线程：" + self.name)
        print(time.time())
        print("退出线程：" + self.name)


for thread_count in range(thread_count):
    thread_count = thread_count + 1
    thread_name = 'Thread-' + str(thread_count)
    myThread(thread_count, thread_name, 1).start()
    # print("运行线程的数量：" + str(threading.active_count()))
