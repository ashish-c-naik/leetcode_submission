class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = 0
        rl = []
        for x in nums:
            s += x
            rl.append(s)
        lr = []
        s = 0
        for x in nums[::-1]:
            s += x
            lr.append(s)
        lr = lr[::-1]
        for index in range(len(lr)):
            if lr[index] == rl[index]:
                return index
        return -1