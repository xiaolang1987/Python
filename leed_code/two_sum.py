#!/user/bin/env python3
# -*- coding: utf-8 -*-

"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""


# 我的答案
def twoSum(nums, target):
    result = []
    tem_list = []
    for i in range(len(nums)):
        n = 1
        for j in nums[i+1:]:
            if j not in tem_list:
                if nums[i] + j == target:
                    result.append(i)
                    result.append(i+n)
                    tem_list.append(nums[i])
                    tem_list.append(j)
                n += 1
    return result


# 通过的答案
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    hashmap = {}
    for index, num in enumerate(nums):
        another_num = target - num
        if another_num in hashmap:
            return [hashmap[another_num], index]
        hashmap[num] = index
    return None


print(twoSum([3, 3, 3, 3], 6))
