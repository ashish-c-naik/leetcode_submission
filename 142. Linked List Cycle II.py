# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head
        f = False
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                f = True
                break
        if f:
            x = head
            while True:
                if x == slow:
                    return x
                x = x.next
                slow = slow.next
        return None