class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        def findlargest(heights):
            i = 0
            position = []
            height = []
            curr = None
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
        self.largest = -1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = 1 if matrix[i][j] == "1" else 0
        curr = []
        for i in range(len(matrix)):
            if i == 0: 
                    curr = matrix[i]
                    findlargest(matrix[i][:])
                    continue
            for j in range(len(matrix[0])):              
                curr[j] = curr[j] + matrix[i][j] if curr[j] != 0 and matrix[i][j] != 0 else matrix[i][j]
            findlargest(curr[:])
            
        return self.largest if self.largest != -1 else 0    
        