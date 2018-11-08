class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if n != 0:
            if m != 0:
                x = m-1

                y = n-1
                z = len(nums1)-1
                while x>-1 and y>-1:
                    if nums1[x] > nums2[y]:
                        nums1[z] = nums1[x]
                        nums1[x] = 0
                        z-=1
                        x-=1
                    else:
                        nums1[z] = nums2[y]
                        z-=1
                        y-=1
                while y >-1:
                    nums1[z] = nums2[y]
                    y-=1
                    z-=1
            else:
                x = 0
                while x < len(nums1):
                    nums1[x] = nums2[x]
                    x+=1
                    
            
        # [2,0]
        # 1
        # [1]
        # 1