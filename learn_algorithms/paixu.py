#!/user/bin/env python3
# -*- coding: utf-8 -*-

"""
学习地址
https://www.cnblogs.com/onepixel/articles/7674659.html
"""


# 冒泡排序
def mao_pao(list_a):
    for l in range(len(list_a)-1, 0, -1):
        for i in range(l):
            if list_a[i] > list_a[i+1]:
                list_a[i], list_a[i+1] = list_a[i+1], list_a[i]
    return list_a


# 插入排序
def cha_ru(list_a):
    for i in range(len(list_a)):
        j = i-1
        key = list_a[i]
        while j >= 0:
            if list_a[j] > key:
                list_a[j+1], list_a[j] = list_a[j], key
            j -= 1
    return list_a


# 选择排序
def xuan_ze(list_a):
    for i in range(len(list_a)):
        min_index = i
        for j in range(i+1, len(list_a)):
            if list_a[j] < list_a[min_index]:
                min_index = j
        list_a[min_index], list_a[i] = list_a[i], list_a[min_index]
    return list_a


list_a = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
# list_a = [11, 22, 1]
print(xuan_ze(list_a))

