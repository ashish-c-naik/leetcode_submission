class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # One line python: 
        # return reduce(lambda a,b:[z+min(x,y) for x,y,z in zip(a,a[1:],b)], triangle[::-1])[0]
        index = 0
        while index < len(triangle) - 1:
            t = [sys.maxint for x in triangle[index+1]]
            for i, val in enumerate(triangle[index]):
                t[i+1] = min(triangle[index+1][i+1] + val, t[i+1])
                t[i] = min(triangle[index+1][i] + val, t[i])
            triangle[index+1] = t
            index += 1
        return min(triangle[-1])
        
        
        