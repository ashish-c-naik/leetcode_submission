class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        i = 0
        position = []
        height = []
        curr = None
        self.largest = -1
        temppos = None
        tempheight = None
        def popthatshit(i, temppos, tempheight, position, height):
            temppos = position[0]
            position = position[1:]
            tempheight = height[0]
            height = height[1:]
            self.largest = max(self.largest, tempheight*(i-temppos))
            return position, height, temppos
        while i < len(heights):
            curr = heights[i]
            if i == 0 or curr > height[0]:
                position = [i] + position
                height = [heights[i]] + height
            elif height and curr < height[0]:
                while height and curr<height[0]: position, height, temppos = popthatshit(i, temppos, tempheight, position, height)
                position = [temppos] + position
                height = [heights[i]] + height
            i+=1
        while height: position, height, temppos = popthatshit(i, temppos, tempheight, position, height)
        return self.largest if self.largest != -1 else 0
                                
                