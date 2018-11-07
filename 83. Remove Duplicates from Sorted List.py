# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        copyofhead = head
        while head:
            curr = head.val
            nodecurr = head
            while head.next and(head.next.val == curr):
                head = head.next
            nodecurr.next = head.next
            head = nodecurr.next
        return copyofhead