#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pip install xlrd  安装读模块
# pip install xlwt 安装写模块
# 参考 https://www.cnblogs.com/MrLJC/p/3715783.html

import xlrd
import xlwt

# 读excel
data = xlrd.open_workbook('zz-test_read.xlsx')
table = data.sheet_by_name('Sheet1') # 通过名称获取sheet
print(table.col_values(0)) # 读取整列

# 写excel
workbook = xlwt.Workbook(encoding='ascii') # 创建excel
worksheet = workbook.add_sheet('123') # 创建sheet
worksheet.write(0, 0, label='Row 0, Column 0 Value') #(列数， 行数， 输入的内容)
workbook.save('zz-Excel_Workbook.xls') # 保存表格

