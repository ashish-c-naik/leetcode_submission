class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        s = nums[:len(nums)//2][::-1]
        l = nums[len(nums)//2:][::-1]
        for i in range(len(nums)):
            if i % 2 == 0 and s and l:
                nums[i] = s.pop()
            elif s and l:
                nums[i] = l.pop()
            elif s and not l:
                nums[i] = s.pop()
            else:
                nums[i] = l.pop()
        
        
                
        