# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        a = head
        b = head
        while b and b.next:
            if b and b.next:
                b = b.next.next
                a = a.next
        return a