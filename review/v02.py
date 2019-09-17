#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class SLinkList(object):
    def __init__(self, itemList):
        if not itemList:
            return None
        self.head = ListNode(itemList[0])
        self.last = self.head
        for item in itemList[1:]:
            newNode = ListNode(item)
            self.last.next = newNode
            self.last = newNode


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        self.head = ListNode(0)
        self.last = self.head
        Quotient = remainder =0
        while l1 or l2:
            numSum = 0
            if l1:
                numSum += l1.val
                l1 = l1.next
            if l2:
                numSum += l2.val
                l2 = l2.next
            remainder = (numSum + Quotient) % 10
            Quotient = (numSum + Quotient) // 10
            newNode = ListNode(remainder)
            self.last.next = newNode
            self.last = newNode
        if Quotient:
            self.last.next = ListNode(1)
        self.last = self.head.next
        return self.last



if __name__ == '__main__':
    l1 = SLinkList([2, 4, 3]).head
    l2 = SLinkList([5, 6, 4]).head
    s = Solution()
    r = s.addTwoNumbers(l1, l2)
    while r:
        print(r.val)
        r = r.next
