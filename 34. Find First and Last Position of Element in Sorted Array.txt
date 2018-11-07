class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans = [-1,-1]
        if nums:
            def findFirst(nums,x,y,target):
                if x<y:
                    mid = (x+y)//2
                    if nums[mid] >= target:
                        y = mid
                    else:
                        x = mid+1
                    return findFirst(nums,x,y,target)
                else:
                    if nums[x] == target:
                        return x
                    else:
                        return -1

            def findLast(nums,x,y,target):
                if x<y:
                    mid = (x+y)//2 + 1
                    if nums[mid] <= target:
                        x = mid 
                    else:
                        y = mid - 1 
                    return findLast(nums,x,y,target)
                else:
                    if nums[y] == target:
                        return y
                    else:
                        return -1
            ans[0] = findFirst(nums,0,len(nums)-1,target)
            ans[1] = findLast(nums,0,len(nums)-1,target)
        return (ans)