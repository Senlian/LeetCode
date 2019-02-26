#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);
示例 1:

输入: s = "LEETCODEISHIRING", numRows = 3
输出: "LCIRETOESIIGEDHN"
示例 2:

输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"
解释:

L     D     R
E   O E   I I
E C   I H   N
T     S     G
'''


class Solution:
    '''
    convert(self, s: 'str', numRows: 'int') -> 'str'
    函数头注释，冒号':'后注明参数类型，'->'后注明返回值类型
    '''
    # 方法一：依次遍历字符串，按列获取元素
    # 时间复杂度：O(n)，其中 n == len(s)。每个索引被访问一次。
    # 空间复杂度：O(n)。
    def convert(self, s: 'str', numRows: 'int') -> 'str':
        if numRows <= 1 or len(s) <= 1 or numRows >= len(s):
            return s
        # 数组每个元素表示一行
        rowArray = [''] * numRows
        # curRow记录当前行
        curRow = 0
        # 记录是否转向
        swerve = False
        for index, item in enumerate(s):
            rowArray[curRow] += item
            if curRow == 0 or curRow == numRows - 1:
                swerve = not swerve
            if swerve:
                curRow += 1
            else:
                curRow -= 1
        print(rowArray)
        return ''.join(rowArray)

    # 方法二：按行获取，interval = 2 * numRows - 2
    # 依据列索引规律，非满元素列与前一元素差为：innergap = interval - 2 * row
    # 时间复杂度：O(n)，其中 n == ((len(s)-2) / interval+1 )*numRows
    # 空间复杂度：O(n)。
    def convert1(self, s: 'str', numRows: 'int') -> 'str':
        if numRows <= 1 or len(s) <= 1 or numRows >= len(s):
            return s
        rowArray = [''] * numRows
        # 首尾行相邻字符的索引间隔，2 * numRows - 2
        interval = 2 * numRows - 2
        for row in range(0, numRows):
            if row == 0:
                rowArray[row] += s[::interval]
            elif row == numRows - 1:
                rowArray[row] += s[(numRows - 1)::interval]
            else:
                # 非首尾行非紧凑相邻字符的索引间隔，2*(numRows-row)-2
                innergap = interval - 2 * row
                for index in range(row, len(s), interval):
                    rowArray[row] += s[index]
                    if index + innergap < len(s):
                        rowArray[row] += s[index + innergap]
        return "".join(rowArray)

    # 方法三：按行获取，interval = 2 * numRows - 2
    # 依据列索引规律，相邻列索引和为interval的倍数
    # 该方法较方法二多计算满元素列，用时较长
    # 时间复杂度：O(n)，其中 n == (len(s)-2 )*numRows。每个索引被访问一次。
    # 空间复杂度：O(n)。
    def convert2(self, s: 'str', numRows: 'int') -> 'str':
        if numRows <= 1 or len(s) <= 1 or numRows >= len(s):
            return s
        rowArray = [''] * numRows
        # 相邻字符串的索引和为(2 * numRows - 2)的倍数
        interval = 2 * numRows - 2

        for row in range(0, numRows):
            if row == 0:
                rowArray[row] += s[::interval]
            elif row == numRows - 1:
                rowArray[row] += s[(numRows - 1)::interval]
            else:
                rowArray[row] += s[row]
                preIndex = row
                for index in range(preIndex+1, len(s)):
                    if (index+preIndex) % interval == 0:
                        rowArray[row] += s[index]
                        preIndex = index
        return "".join(rowArray)

if __name__ == '__main__':
    s = "PAYPALISHIRING"
    print(len(s))
    func = Solution()
    rst = func.convert(s, 4)
    rst1 = func.convert1(s, 4)
    rst2 = func.convert2(s, 4)
    print(rst)
    print(rst1)
    print(rst2)
