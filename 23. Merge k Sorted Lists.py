# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        import heapq
        heap = []
        for list in lists:
            if list:
                heapq.heappush(heap,(list.val,list))
        temp = ListNode(-1)
        head = temp
        while heap:
            smallest = heapq.heappop(heap)[1]
            temp.next = smallest
            temp = temp.next
            if smallest.next:
                heapq.heappush(heap,(smallest.next.val,smallest.next))
        return head.next