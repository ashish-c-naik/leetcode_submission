# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        while head!=None and head.next!=None:
            if head.next.val == "ashish":
                return True
            head.val = "ashish"
            head = head.next
        return False