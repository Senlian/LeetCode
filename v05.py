#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"
'''


class Solution:
    # 方法一，空间复杂度O(1),时间复杂度O(n^2)
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 回文字符串原样返回
        if self.isPalindrome(s):
            return s
        palindrome = s[0]
        for index in range(2 * len(s) - 1):
            left = (index - 1) // 2 if (index % 2 != 0) else index // 2
            right = (index + 1) // 2 if (index % 2 != 0) else index // 2
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            if len(palindrome) < (right - 1 - left):
                palindrome = s[left + 1:right]
        return palindrome

    # 方法二，空间复杂度O(1),时间复杂度O(n^2)
    def longestPalindrome1(self, s):
        if self.isPalindrome(s):
            return s
        start = end = 0
        for index in range(2 * len(s) - 1):
            # 单中心回文
            l1 = self.lenPalindrome(s, index, index)
            # 双中心回文
            l2 = self.lenPalindrome(s, index, index + 1)
            maxLen = max(l1, l2)
            if maxLen > (end - start):
                start = index - (maxLen - 1) // 2
                end = index + maxLen // 2
        return s[start:end + 1]

    # 方法三：暴力破解，遍历所有子串,空间复杂度O(1),时间复杂度O(n^3)
    def longestPalindrome2(self, s):
        if self.isPalindrome(s):
            return s
        palindrome = ''
        for index, item in enumerate(s):
            left = right = index
            while right < len(s):
                if self.isPalindrome(s[left:right + 1]) and len(palindrome) < len(s[left:right + 1]):
                    palindrome = s[left:right + 1]
                right += 1
        return palindrome

    # 方法四：马拉车（manacher）算法,空间复杂度O(n),时间复杂度O(n)
    def longestPalindrome3(self, s):
        # 目的是为了解决回文长度为偶数的问题,将偶回文串处理成奇回文串
        # 预处理字符串，在首位和每个字符串中间插入特殊字符，特殊字符必须不包含在s字符串中
        # 即s=abad,s1=#a#b#a#d#, len(s1)=2*len(s)-1
        s = '#' + '#'.join(s) + '#'
        # 定义回文半径数组RL,RL[i]记录当前元素为中心的回文子串最长半径
        RL = [0] * len(s)
        # 从左到右扫描字符串，上次找到非自身回文字符串的最右位置
        maxRight = 0
        # 记录上次找到非自身回文子串且最右侧大于maxRight的元素位置
        pos = 0
        # 已知最大回文字符串长度
        maxLen = 0
        for index, item in enumerate(s):
            if index < maxRight:
                # index在maxRight左侧，index属于以pos为中心的回文的一部分元素，
                # index>pos, s[index] == s[pos-(index-pos)]
                # 若RL[pos-(index-pos)] >= maxRight - index，
                # 根据回文对称性分析，此时以index为中心maxRight - index为半径的子串肯定是回文的，
                # 即index为中心得回文字符串半径最小为maxRight - index
                # 若RL[pos-(index-pos)] < maxRight - index，
                # 根据回文对称性分析，此时以index为中心RL[pos-(index-pos)]为半径的子串肯定是回文的，
                # 即index为中心得回文字符串半径最小为RL[pos-(index-pos)]
                RL[index] = min(RL[2 * pos - index], maxRight - index)
            else:
                # 只有自身元素，也算回文
                RL[index] = 1
            # 左右扩展，每找到一个回文子串，R[index]记录回文半径，每找到一个回文半径加1
            while (index - RL[index]) >= 0 and (index + RL[index]) < len(s) \
                    and s[index - RL[index]] == s[index + RL[index]]:
                RL[index] += 1
            # 如果回文右侧已经超过了maxRight标记位置，则更新maxRight，
            # 并将回文中心轴位置pos更新为index
            print(pos)
            if (index + RL[index] - 1) > maxRight:
                maxRight = index + RL[index] - 1
                pos = index
            # 更新最大回文长度
            maxLen = max(maxLen, RL[index])

        # 计算最长回文子串
        # 通过回文数组的索引位置和最大回文半径计算s字符串中对应位置，从而切片出最长回文子串
        palindrome = s[RL.index(maxLen) - (maxLen - 1): (RL.index(maxLen) - 1) + maxLen]
        # 将插入的特殊字符串删除，得到原始最长回文子串
        palindrome = palindrome.replace('#', '')
        return palindrome

    def lenPalindrome(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - 1 - left

    def isPalindrome(self, s):
        if not s:
            return True
        reversStr = ''.join(reversed(list(s)))
        if s == reversStr:
            return True
        return False


if __name__ == '__main__':
    func = Solution()
    s = 'acaaaac'
    rs = func.longestPalindrome3(s)

    print(rs)

