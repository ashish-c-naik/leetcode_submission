class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = [1,2,2]
        i = 2
        j = 2
        curr = 1
        curr_len = 0
        while j < n:
            for _ in range(l[i]):
                l.append(curr)
            j+=l[i] 
            i+=1
            curr = (2,1)[curr==2]
        
        return sum([(0,1)[x==1] for x in l[:n]])