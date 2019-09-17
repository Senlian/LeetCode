#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
'''


class Solution1(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        lenAll = len(s)
        lenSet = len(set(s))

        if lenAll == lenSet:
            return lenAll
        if lenSet == 1:
            return lenSet

        targetDict = {}
        lastIndex = lenCur = 0
        for index, item in enumerate(s):
            if item in targetDict:
                # 前一个重复元素的下标
                findIndex = targetDict[item]
                # 下一次开始查找的下标
                lastIndex = max(lastIndex, findIndex)
            # 当前下标-前一个重复数下标+1=无重复数长度
            lenCur = max(lenCur, index - lastIndex + 1)
            # 向后查找记录前一个元素的下标
            targetDict[item] = index + 1
        return lenCur


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :desc: 双指针发求解，移动右边指针，当右边与左边有重复移动左边指针
        :type s: str
        :rtype: int
        """
        items = ''
        maxLen = 0
        curItems = ''
        for index, item in enumerate(s):
            # 找到重复字符，记录无重复串，移动左边指针到找到的重复元素的下一元素重新开始找无重复串
            if item in items:
                if maxLen <= len(items):
                    curItems = items
                if index + 1 != len(s):
                    items = items[items.index(item) + 1:]
            # 没有找到重复字符，则将字符添加到串
            if item not in items:
                items += item
            # 记录最大长度
            maxLen = max(maxLen, len(items))
        print(curItems)
        return maxLen


if __name__ == '__main__':
    # s = ' '
    # s = 'ab ba'
    # s = 'dvdf'
    s = 'aabdedc!ddca'
    t = Solution()
    r = t.lengthOfLongestSubstring(s)
    print(r)
