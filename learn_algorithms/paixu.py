#!/user/bin/env python3
# -*- coding: utf-8 -*-

"""
学习地址
https://www.cnblogs.com/onepixel/articles/7674659.html
"""


# 冒泡排序
def mao_pao(array):
    for l in range(len(array)-1, 0, -1):
        for i in range(l):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
    return array


# 插入排序
def cha_ru(array):
    for i in range(len(array)):
        j = i-1
        key = array[i]
        while j >= 0:
            if array[j] > key:
                array[j+1], array[j] = array[j], key
            j -= 1
    return array


# 选择排序
def xuan_ze(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i+1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[min_index], array[i] = array[i], array[min_index]
    return array


# 快排
def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [s for s in array[1:] if s <= pivot]
        greater = [s for s in array[1:] if s >= pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


array = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
# array = [11, 22, 1]
print(quick_sort(array))


