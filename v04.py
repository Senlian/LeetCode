#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5
'''
a = [1, 1, 2]


# TODO: 归并排序求中位数
class Solution1:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums3 = []
        nums3.extend(nums1)
        nums3.extend(nums2)
        nums3 = sorted(nums3)
        midIndex = len(nums3) // 2

        if len(nums3) % 2:
            return float(nums3[midIndex])
        return (nums3[midIndex - 1] + nums3[midIndex]) / 2


# TODO: 桶排序求中位数
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        minList, maxList, minLen, maxLen = nums1, nums2, len(nums1), len(nums2)
        if minLen > maxLen:
            minList, maxList, minLen, maxLen = maxList, minList, maxLen, minLen
        if maxLen == 0:
            raise ValueError

        curson, size, half = 0, minLen, (minLen + maxLen + 1) // 2
        while curson <= size:
            '''
            目标：将长、短列表分别划分为左右两部分，使得左部总长度等于右部总长度且左部的值始终小于右部的值。
            minList = minListLeft + minListRight
            maxList = maxListLeft + maxListRight
            len(minListLeft+maxListLeft) = len(minListRight+maxListRight) = half
            '''
            minListLeftLen = (curson + size) // 2
            maxListLeftLen = half - minListLeftLen
            '''
            minList = minListLeft                 + minListRight
            minList = minList[0:minListLeftLen] + minList[minListLeftLen:]
            maxList = maxListLeft                 + maxListRight
            maxList = maxList[0:maxListLeftLen] + maxList[maxListLeftLen:]
            '''
            # max(maxListLeft) > min(minListRight)
            # 违反左部值小于右部值原则，则短列表右部最小元素划入左部元素，
            # 即将短列表的左侧部分长度加1
            if minListLeftLen < minLen and maxList[maxListLeftLen - 1] > minList[minListLeftLen]:
                curson = minListLeftLen + 1
            # max(minListLeft) > min(maxListRight)
            # 违反左部值小于右部值原则，则长列表右部最小元素划入左部元素
            # 将长列表的左侧部分长度加1，即将短列表的左侧部分长度减一
            elif minListLeftLen > 0 and minList[minListLeftLen - 1] > maxList[maxListLeftLen]:
                size = minListLeftLen - 1
            # 左右划分完毕，开始计算中位数的值
            else:
                # 左部全部为长列表元素
                if minListLeftLen == 0:
                    max_num_left = maxList[maxListLeftLen - 1]
                # 左部全部为短列表元素
                elif maxListLeftLen == 0:
                    max_num_left = minList[minListLeftLen - 1]
                # 长短列表都有左部元素，则左部都为较小值，取最大值参与中位数运算
                else:
                    max_num_left = max(minList[minListLeftLen - 1], maxList[maxListLeftLen - 1])
                # 奇数个元素，左部元素为偶数个，即中位数在左部最右侧
                if (minLen + maxLen) % 2 == 1:
                    return max_num_left
                # 短列表右部长度为0，则右部最小值为长列表右部最左侧值
                if minListLeftLen == minLen:
                    min_num_right = maxList[maxListLeftLen]
                # 长列表右部长度为0，则右部最小值为短列表右部最左侧值
                elif maxListLeftLen == maxLen:
                    min_num_right = minList[minListLeftLen]
                # 长短列表都有右部元素，则右部都为较大值，取最小值参与中位数运算
                else:
                    min_num_right = min(minList[minListLeftLen], maxList[maxListLeftLen])
                # 中位数为:(左部最大值+右部最小值)/2
                return float((max_num_left + min_num_right) / 2)


if __name__ == '__main__':
    nums1 = [2, 3, 4]
    nums2 = [1]

    s = Solution()
    rst = s.findMedianSortedArrays(sorted(nums1), sorted(nums2))
    # rst1 = median(nums1, nums2)
    print(rst)
    # print(rst1)
