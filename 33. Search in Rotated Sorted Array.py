class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        def binary_findmin(nums,x,y):
            if x >= y - 1:
                return y
            else:
                mid = (x+y) // 2
                if nums[mid] > nums[y]:
                    x = mid
                else:
                    y = mid
                return binary_findmin(nums,x,y)
        min_pos = binary_findmin(nums,0,len(nums) - 1)
        def bin_search(nums,target,x,y):
            if x > y:
                return -1
            else:
                mid = (x+y) // 2
                if nums[mid] == target:
                    return mid
                if nums[mid] < target:
                    x = mid + 1
                else:
                    y = mid - 1
                return bin_search(nums,target,x,y)
        return max(bin_search(nums,target,0,min_pos-1), bin_search(nums,target,min_pos,len(nums)-1))