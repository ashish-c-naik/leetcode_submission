class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxnum = 0
        maxpos = 0
        total = 0
        blocks = 0
        for index,x in enumerate(height):
            if maxnum <= x:
                total += (index-maxpos-1)*maxnum - blocks
                blocks = 0
                if index < len(height) -1:
                    if max(height[index+1:]) >= x:
                        maxnum = x
                        maxpos = index
                    else:
                        maxnum = max(height[index+1:])
                        maxpos = index
            else:
                blocks += x
        return total