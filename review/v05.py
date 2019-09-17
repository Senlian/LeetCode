#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if self.isPalindrome(s):
            return s
        palindrome = s[0]
        for index in range(2 * len(s) - 1):
            left = (index - 1) // 2 if index % 2 else index // 2
            right = (index + 1) // 2 if index % 2 else index // 2
            while left >=0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            if len(palindrome) < (right - left -1):
                palindrome = s[left+1:right]
        return palindrome

    def isPalindrome(self, s):
        if not s or s == ''.join(reversed(list(s))):
            return True
        return False


if __name__ == '__main__':
    s = "acaaaac"
    i = Solution()
    print(i.longestPalindrome(s))
