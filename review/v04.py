#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# 归并排序法
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        short, long, minlen, maxlen = nums1, nums2, len(nums1), len(nums2)
        if minlen > maxlen:
            short, long, minlen, maxlen = long, short, maxlen, minlen
        if not maxlen:
            return ValueError
        left, right, half = 0, minlen, (minlen + maxlen + 1) // 2

        while left <= right:
            shortleft = (left + right) // 2
            longleft = half - shortleft
            if shortleft > 0 and short[shortleft - 1] > long[longleft]:
                right = shortleft - 1
            elif shortleft < minlen and long[longleft - 1] > short[shortleft]:
                left = shortleft + 1
            else:
                if not shortleft:
                    max_left = long[longleft - 1]
                elif not longleft:
                    max_left = short[shortleft - 1]
                else:
                    max_left = max(long[longleft - 1], short[shortleft - 1])

                if (minlen + maxlen) % 2:
                    return float(max_left)
                if shortleft == minlen:
                    min_right = long[longleft]
                elif longleft == maxlen:
                    min_right = short[shortleft]
                else:
                    min_right = min(long[longleft], short[shortleft])
                return (min_right + max_left) / 2.0
        return None


if __name__ == '__main__':
    nums1 = [2, 3, 4]
    nums2 = [1]
    s = Solution()
    print(s.findMedianSortedArrays(nums1, nums2))
