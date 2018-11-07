class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        l = [d for row in nums for d in row]
        ans = []
        for i in range(r):
            row = []
            for j in range(c):
                if not l:
                    return nums
                row.append(l[0])
                l = l[1:]
            ans.append(row)
        return ans