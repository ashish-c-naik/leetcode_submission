# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        l = 0
        headcopy = head
        while head:
            l += 1
            head = head.next
        def r(head,l):
            if head==None or l <= 0:
                return head, True
            elif l == 1:
                return head.next, True
            result = r(head.next, l - 2)
            res =  (result[0].val == head.val) and result[1]
            return result[0].next, res
        return r(headcopy,l)[1]