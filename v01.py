#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''
nums = [3, 3]
target = 6
from copy import copy, deepcopy


class Solution1(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) < 2:
            return
        numList = deepcopy(nums)
        for index1, num in enumerate(nums):
            rst = target - num
            # 排除自身元素
            if rst == num:
                numList[index1] = None
            if rst in numList:
                return index1, numList.index(rst)

# TODO: 字典hash,降低复杂度
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) < 2:
            return

        indexDict = {}
        for index, num in enumerate(nums):
            rst = target - num
            if rst not in indexDict:
                indexDict[num] = index
            else:
                return [indexDict.get(rst), index]

if __name__ == '__main__':
    s = Solution()
    print(s.twoSum(nums, target))
