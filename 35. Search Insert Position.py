class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def bins(nums,target,x,y):
            if x > y:
                return x
            else:
                mid = (x+y) // 2
                if nums[mid] == target:
                    return mid
                if nums[mid] > target:
                    y = mid - 1
                else:
                    x = mid + 1
                return bins(nums,target,x,y)
        return bins(nums,target,0,len(nums)-1)