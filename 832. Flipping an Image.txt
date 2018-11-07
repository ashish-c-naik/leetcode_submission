class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return [[0 if y==1 else 1 for y in x[::-1]]for x in A]
       
        