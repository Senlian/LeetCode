# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class SLinkList(object):
    def __init__(self, itemList):
        if not itemList:
            return
        self.head = ListNode(itemList[0])
        self.last = self.head
        for item in itemList[1:]:
            newNode = ListNode(item)
            self.last.next = newNode
            self.last = newNode



class Solution1(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1

        Quotient = 0
        remainder = 0
        headNode = ListNode(0)
        lastNode = headNode

        while l1 or l2:
            itemSum = 0
            if l1:
                itemSum += l1.val
                print('itemSum1=',itemSum)
                l1 = l1.next
            if l2:
                itemSum += l2.val
                print('itemSum2=', itemSum)
                l2 = l2.next
            print('itemSum=',itemSum)
            print('Quotient=',Quotient)
            # yushu,
            remainder = (itemSum + Quotient) % 10
            # shang
            Quotient = (itemSum + Quotient) // 10

            # print(itemSum, remainder,Quotient)

            newNode = ListNode(remainder)
            lastNode.next = newNode
            lastNode = newNode
        if Quotient:
            lastNode.next = ListNode(1)
        lastNode = headNode.next
        del headNode
        return lastNode


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1

        Quotient = 0
        remainder = 0
        headNode = ListNode(0)
        lastNode = headNode

        while l1 or l2:
            itemSum = 0
            if l1:
                itemSum += l1.val
                l1 = l1.next

            if l2:
                itemSum += l2.val
                l2 = l2.next
            # print(itemSum)
            # yushu
            remainder = (itemSum + Quotient) % 10
            # shang
            Quotient = (itemSum + Quotient) // 10

            # print(itemSum, remainder,Quotient)

            newNode = ListNode(remainder)
            lastNode.next = newNode
            lastNode = newNode
        if Quotient:
            lastNode.next = ListNode(Quotient)
        return headNode.next


if __name__ == "__main__":
    l1 = SLinkList([1, 2, 5]).head
    l2 = SLinkList([9, 4, 5]).head
    s = Solution()
    rst = s.addTwoNumbers(l1, l2)
    while rst:
        print(rst.val)
        rst = rst.next
