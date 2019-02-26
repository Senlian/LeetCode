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
                findIndex = targetDict[item]
                lastIndex = max(lastIndex, findIndex)
            lenCur = max(lenCur, index - lastIndex + 1)
            targetDict[item] = index + 1
        return lenCur


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        items = ''
        maxLen = 0
        curItems = ''
        for index, item in enumerate(s):
            if item in items:
                if maxLen <= len(items):
                    curItems = items
                if index + 1 != len(s):
                    items = items[items.index(item) + 1:]
            if item not in items:
                items += item
            maxLen = max(maxLen, len(items))
        print(curItems)
        return maxLen


if __name__ == '__main__':
    # s = ' '
    # s = 'ab ba'
    # s = 'dvdf'
    s = 'aabdedc!ddca'
    t = Solution1()
    r = t.lengthOfLongestSubstring(s)
    print(r)
