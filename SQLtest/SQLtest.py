#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import pymysql

db = pymysql.connect('101.201.73.129', 'reader', '8TDURgAtWcYU6rTm', 'turing_platform_log', 3318, charset="utf8")

cursor = db.cursor()
sql_select = 'SELECT * FROM platform_cloud_log_201805 WHERE apikey IN ("108bd270ef2d489f8bf714fde5ece5fc","aecdc3aa66824f6a9c84ac1b1531e698","05e7822d0cf14a22bd7aa37deafe7b60","3c03046e3bdd4594bf9f4b4337575f50","c099c14ffcbe4cc9ae5b0797e0555209","57e62a88572e4d4e811325c1bbce35b5","573f9f6108ef44f5a4f8f31110c5bf73")AND((create_date >= "2018-05-23 12:00:00" AND create_date <= "2018-05-23 13:59:59")) ORDER BY apikey LIMIT 10'
data = cursor.execute(sql_select.encode('utf-8'))
results = cursor.fetchall()
f_out = open("result.txt", "w", encoding="utf-8")
for row in results:
    f_out.write(str(row[0]) + "\t")
    f_out.write(row[1] + "\t")
    f_out.write(row[2] + "\t")
    f_out.write(row[3] + "\t")
    f_out.write(row[4] + "\t")
    f_out.write(row[5] + "\t")
    f_out.write(str(row[6]) + "\t")
    f_out.write(str(row[7]) + "\t")
    f_out.write(str(row[8]) + "\t")
    f_out.write(str(row[9]) + "\t")
    f_out.write(row[10] + "\t")
    f_out.write(str(row[11]) + "\t")
    f_out.write(str(row[12]) + "\t")
    try:
        f_out.write(row[13] + "\t")
    except:
        f_out.write(" " + "\t")
    try:
        f_out.write(row[14] + "\t")
    except:
        f_out.write(" " + "\t")
    f_out.write(row[15] + "\n")

f_out.close()



