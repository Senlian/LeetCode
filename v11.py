#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。



图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
https://leetcode-cn.com/problems/container-with-most-water/


示例:

输入: [1,8,6,2,5,4,8,3,7]
输出: 49
'''


class Solution:
    # 暴力法,O(n**2),O(1)
    def maxArea(self, height: 'List[int]') -> 'int':
        areaMax = 0
        length = len(height)
        for left in range(0, length):
            for right in range(left + 1, length):
                areaMax = max(areaMax, (right - left) * min(height[left], height[right]))
        return areaMax

    # 方法二：双指针法,O(n),O(1)
    def maxArea1(self, height: 'List[int]') -> 'int':
        areaMax = 0
        length = len(height)
        left, right = 0, length - 1
        while left < right:
            areaMax = max(areaMax, min(height[left], height[right]) * (right - left))
            # 短线指针向长线指针移动
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return areaMax


if __name__ == '__main__':
    f = Solution()
    area = f.maxArea1([1, 15, 56, 2, 5, 54, 8, 3, 17])
    print(area)
