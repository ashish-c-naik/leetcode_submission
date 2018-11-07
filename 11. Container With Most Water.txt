class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        x = 0
        y = len(height)-1
        maxi = 0
        while x < y:
            curr = min(height[x],height[y])*(y-x)
            maxi = max(maxi,curr)
            if height[x] > height[y]:
                y -= 1
            else:
                x += 1
        return maxi
        