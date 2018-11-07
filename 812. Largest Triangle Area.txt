class Solution(object):
    def area(self,l1,l2,l3):
        return .5 * abs(l1[0]*l2[1]+l2[0]*l3[1]+l3[0]*l1[1]
                           -l1[1]*l2[0]-l2[1]*l3[0]-l3[1]*l1[0])
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        import itertools
        m = -1
        for x in itertools.combinations(points,3):
            m = max(m,self.area(x[0],x[1],x[2]))
        return m