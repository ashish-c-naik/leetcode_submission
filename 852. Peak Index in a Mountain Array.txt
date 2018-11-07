class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        peakheight = -1
        peakindex = -1
        incr = True
        for index,value in enumerate(A):
            if incr and index == 1 and A[index - 1] > A[index]:
                return 0
            elif incr and A[index-1] > A[index]:
                incr = False
            elif A[index-1] < A[index]:
                if not incr:
                    incr = True
                if peakheight < value:
                    peakheight = value
                    peakindex = index
        return peakindex