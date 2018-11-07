class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        l = {0:0,1:1,2:5,5:2,6:9,8:8,9:6}
        count=0
        def isgood(l,number):
            new = ""
            for x in number:
                if int(x) in l:
                    new += str(l[int(x)])
                else:
                    return False
            return not new == number
        for x in range(N+1):
            if isgood(l,str(x)):
                count+=1
        return count
            
                
                
        