#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution(object):
    def threeSum1(self, nums):
        """
        :desc: 暴力拆解，先转换为量数之和，再求解
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        lists = []
        for index, num in enumerate(nums):
            target = 0 - num
            nlists = self.twoSum(nums, target)
            if not nlists:
                continue
            for nlist in nlists:
                if nlist and index not in nlist:
                    nlist.append(index)
                    nlist.sort()
                    l = [nums[i] for i in nlist]
                    l.sort()
                    if l not in lists:
                        lists.append(l)
        return lists

    def twoSum(self, numbs, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(numbs) < 2:
            return

        indexDict = {}
        lists = []
        for index, num in enumerate(numbs):
            rst = target - num
            if rst not in indexDict:
                indexDict[num] = index
            else:
                lists.append([indexDict.get(rst), index])
        return lists

    def threeSum(self, nums):
        """
        :desc: 双指针
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 按大小排序
        nums.sort()
        # i记录从左到右扫描数的下标
        rsts, target = [], 0
        for target in range(len(nums)):
            # 左部最小数大于0，则右部两数之和肯定大于0，没有满足的组合
            if nums[target] > 0:
                break
            # 从记录数的下一个下标开始扫描，直到数组结尾
            left, right = target + 1, len(nums) - 1
            # 跳过重复数，避免重复扫描
            if target > 0 and nums[target] == nums[target - 1]:
                continue
            # 执行扫描
            while left < right:
                # 三数之和
                sums = nums[target] + nums[left] + nums[right]
                # 不满足情况1，小于0 把左指针右移
                if sums < 0:
                    left += 1
                    # 跳过重复情况
                    while left < right and nums[left] == nums[left - 1]: left += 1
                # 不满足情况1，大于0 把右指针左移
                elif sums > 0:
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]: right -= 1
                # 满足条件，添加组合，跳过重复数，左右指针同时向中间移动
                else:
                    rsts.append([nums[target], nums[left], nums[right]])
                    # 左右指针向中间移动查找下一个满足条件的组合
                    left += 1
                    right -= 1
                    # 左右指针标识组合数相同情况跳过
                    while left < right and nums[left] == nums[left - 1]: left += 1
                    while left < right and nums[right] == nums[right + 1]: right -= 1

        return rsts


if __name__ == '__main__':
    # nums = [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]
    nums = [-1, 0, 1, 2, -1, -4]

    s = Solution()
    print(s.threeSum(nums))
