#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2**31,  2**31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
'''


class Solution:
    def reverse(self, x: 'int') -> 'int':
        if not x:
            return x
        x = str(x).rstrip('0')
        minus = True if '-' in x else False
        x = x.lstrip('-')
        x = int(x[::-1]) if not minus else 0 - int(x[::-1])
        if -2 ** 31 < x < 2 ** 31 - 1:
            return x
        return 0

    def reverse1(self, x: 'int') -> 'int':
        if not x:
            return x
        reversX = 0
        minus = True if x < 0 else False
        Quotient = x if not minus else -x
        while Quotient > 0:
            remainder = Quotient % 10
            Quotient = Quotient // 10
            reversX = reversX * 10 + remainder
        reversX = int(reversX) if not minus else -int(reversX)
        if -2 ** 31 < reversX < 2 ** 31 - 1:
            return reversX
        return 0


if __name__ == '__main__':
    func = Solution()
    x = func.reverse1(-123)
    print(x)
    print(-2 ** 31)
    print(2 ** 31 - 1)
    print(9646324351 > 2 ** 31 - 1)
