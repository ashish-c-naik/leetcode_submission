class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        fl = []
        bl = []
        m = 1
        for x in nums:
            m *= x
            fl.append(m)
        m = 1
        for x in nums[::-1]:
            m *= x
            bl.append(m)
        bl = bl[::-1]
        ans = []
        for x in range(len(fl)):
            if x == 0 and x < len(bl) - 1:
                ans.append(bl[x+1])
            else:
                if x < len(bl) - 1:
                    ans.append(fl[x-1] * bl[x+1])
                else:
                    ans.append(fl[x-1])
        return ans
        