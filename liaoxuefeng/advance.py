#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 高级特性练习题


# 切片
def qie_pian(arr):
    print("显示前三个元素" + str(L[:3]))
    print("显示第三个之后的元素" + str(L[3:]))
    print("间隔两个显示" + str(L[::3]))


# 迭代
def iteration(arr):
    for i in range(1, len(arr)):
        if arr[i-1] > arr[i]:
            arr[i-1], arr[i] = arr[i], arr[i-1]
    maxarr = arr[-1]

    for i in range(len(arr)-1, 0, -1):
        if arr[i-1] > arr[i]:
            arr[i], arr[i-1] = arr[i-1], arr[i]
    minarr = arr[0]
    return maxarr, minarr


# 列表生成式
def lie_biao_sheng_cheng_shi():
    L1 = ['Hello', 'World', 18, 'Apple', None]
    L2 = [s.lower() for s in L1 if isinstance(s, str)]
    print(L2)


if __name__ == "__main__":
    L = [5, 8, 2, 10, 1]
    qie_pian(L)
    print(iteration(L))
    lie_biao_sheng_cheng_shi()



