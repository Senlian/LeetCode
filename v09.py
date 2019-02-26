#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
进阶:

你能不将整数转为字符串来解决这个问题吗？
'''


class Solution:
    def isPalindrome(self, x: 'int') -> 'bool':
        if 0 <= x <= 9:
            return True
        s = str(x)
        if not s:
            return True
        reversStr = ''.join(reversed(list(s)))
        if s == reversStr:
            return True
        return False

    def isPalindrome1(self, x: 'int') -> 'bool':
        if 0 <= x <= 9:
            return True
        if x < 0:
            return False
        reverseX = self.reverse(x)
        if reverseX == x:
            return True
        return False

    def reverse(self, x: 'int') -> 'int':
        if not x:
            return x
        reversX = 0
        Quotient = x
        while Quotient > 0:
            remainder = Quotient % 10
            Quotient = Quotient // 10
            reversX = reversX * 10 + remainder
        reversX = int(reversX)
        return reversX



if __name__ == '__main__':
    func = Solution()
    rst = func.isPalindrome1(10)
    print(rst)
