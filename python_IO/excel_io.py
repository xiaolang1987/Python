#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pip install xlrd  安装读模块
# pip install xlwt 安装写模块
# 参考    https://www.cnblogs.com/MrLJC/p/3715783.html
#           https://www.cnblogs.com/linyfeng/p/7123423.html

import xlrd
import xlwt

# 读excel
data = xlrd.open_workbook('zz-test_read.xlsx')
"""读取整列数据"""
table = data.sheet_by_name('Sheet1') # 通过名称获取sheet
print(table.col_values(0)[1:]) # 读取整列
for a in table.col_values(0)[1:]:
    if a:
        print(a)
"""获取所有sheet"""
print(data.sheet_names())
"""获取sheet名字"""
print(data.sheet_names()[1])
"""获取单元格数据类型"""
print(table.cell(0, 0).ctype) # ctype : 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
"""强制转换数字"""
number = 6.0
if number == int(number):
    int(number)
else:
    number = number
""""""
""""""
""""""
""""""
""""""
# 写excel
# workbook = xlwt.Workbook(encoding='ascii') # 创建excel
# worksheet = workbook.add_sheet('123') # 创建sheet
# worksheet.write(0, 0, label='Row 0, Column 0 Value') #(行数， 列数， 输入的内容)
# workbook.save('zz-Excel_Workbook.xls') # 保存表格
