class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        def r(ans,arr,stack):
            if arr:
                for x in arr:
                    prev = stack[:]
                    l = arr[:]
                    l.remove(x)
                    stack.append(x)
                    if len(stack) == len(nums):
                        ans.append(stack)
                        return ans
                    else:
                        ans = r(ans,l,stack)
                    stack = prev
            return ans
        return r([],nums,[])
                