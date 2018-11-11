# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addLists(self, number_of_times, size_of_each, root):
        """
        Create linkedList of "size_of_each" size and append to the
        ans list "number_of_times" this many number of times
        and return the changed root
        """
        while root and number_of_times:
            l1 = ListNode(None)
            head = l1
            size_of_each_1 = size_of_each
            while root and size_of_each_1:
                l1.next = ListNode(root.val)
                l1 = l1.next
                root = root.next
                size_of_each_1 -= 1
            self.ans.append(head.next)
            number_of_times -= 1
        return root
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        import math
        self.ans = []
        length = 0
        head = root
        while root: 
            length += 1
            root = root.next
        root = head
        if length % k == 0 or length / k < 1:
            c = math.ceil(float(length) / k)
            x = length
            f = 0
            y = 0
        elif length/k >= 1:
            c = math.ceil(float(length)/k)
            f = math.floor(float(length)/k)
            x = (length - f*k)/(c-f)
            y = k-x
        root = self.addLists(x, c, root)
        root = self.addLists(y, f, root)
        if len(self.ans) == k: return self.ans
        else:
            for x in range(k-len(self.ans)): self.ans.append([])
        return self.ans