#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def reverse(self, x: int) -> int:

        if -9 < x < 9:
            return x
        flag = False
        if x < 0:
            flag = True
            x = -x
        num =0
        while x:
            r = x % 10
            x = x // 10
            num = num*10 +r
        num = int(num) if not flag else -int(num)
        if -2**31 < num < 2**31 -1:
            return num
        return 0





if __name__ == '__main__':
    x = 123

    s = Solution()
    print(s.reverse(x))
