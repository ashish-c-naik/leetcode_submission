# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return
        head1 = headA
        head2 = headB
        len1 = 0
        len2 = 0
        while head1 and head1.next:
            len1 += 1
            head1 = head1.next
        while head2 and head2.next:
            len2 += 1
            head2 = head2.next
        if head1 != head2:
            return None
        len1 += 1
        len2 += 1
        diff = abs(len1 - len2)
        if len1 > len2:
            large = headA
            small = headB
        else:
            large = headB
            small = headA
        while diff:
            large = large.next
            diff -= 1
        while large.next and small.next and large != small:
            large = large.next
            small = small.next
        return large
        