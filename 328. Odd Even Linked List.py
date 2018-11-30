# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return head
        x = head
        y = head.next
        z = y
        while x and z and x.next and z.next:
            x.next = x.next.next
            z.next = z.next.next
            x = x.next
            z = z.next
        x.next = y
        return head