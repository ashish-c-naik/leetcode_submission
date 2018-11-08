# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        def which(x,y):
            if x == y:
                return x
            else:
                mid = (x+y) // 2
                if isBadVersion(mid):
                    return which(x,mid)
                else:
                    return which(mid+1,y)
        return which(1,n)