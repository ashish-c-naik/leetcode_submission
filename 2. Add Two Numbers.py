# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def lengthof(self,l):
        count = 0
        while l:
            l = l.next
            count+=1
        return count
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if self.lengthof(l1) < self.lengthof(l2):
            l1,l2 = l2,l1
        copyl1 = l1
        copyl2 = l2
        l3 = ListNode(0)
        headofl3 = l3
        carry = 0
        sumof = 0
        f = True
        while f:
            print(l1.val)
            sumof = l1.val
            if l1.next:
                l1 = l1.next
            else:
                f = False
            if l2:
                sumof+=l2.val
                if l2.next:
                    l2 = l2.next
                else:
                    l2 = None
            if carry != 0:
                sumof+= carry
            l3.next = ListNode(sumof % 10)
            l3 = l3.next
            carry = sumof / 10
            print("carry ",carry)
        if carry > 0:
            l3.next = ListNode(carry)
        return headofl3.next      
        