#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。
返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum-closest
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def threeSumClosest(self, nums: 'List[int]', target: int) -> int:
        nums.sort()
        # 正无穷float('inf')，负无穷float('-inf')
        ans = float('inf')
        for key in range(len(nums)):
            left, right = key + 1, len(nums) - 1
            if key >0 and nums[key] == nums[key-1]:
                continue
            while left < right:
                sums = nums[key] + nums[left] + nums[right]
                if abs(target-sums) < abs(target-ans):
                    ans = sums
                if sums > target:
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]: right -= 1
                elif sums < target:
                    left += 1
                    while left < right and nums[left] == nums[left - 1]: left += 1
                else:
                    return ans
        return ans


if __name__ == '__main__':
    nums = [1,1,1,0]
    target = 100
    s = Solution()
    print(s.threeSumClosest(nums,target))
