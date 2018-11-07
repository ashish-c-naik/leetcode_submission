class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) > 1:
            x = -1
            y = len(nums)
            z = 0
            while z< y:
                while -1 < z < len(nums) and  nums[z] == 1:
                    z+=1
                if z<y:
                    if len(nums) > z > -1 and nums[z] == 2:
                        y-=1
                        nums[y],nums[z] = nums[z],nums[y]
                        if y==z:
                            break
                    if len(nums) > z > -1 and nums[z] == 0:
                        x+=1
                        nums[x], nums[z] = nums[z], nums[x]
                        if x==z:
                            z+=1
