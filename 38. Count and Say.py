class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = "1"
        while n>1:
            count = x = 0
            prev = ans[0]
            newans = ""
            while x<len(ans):
                while x < len(ans) and prev == ans[x]:
                    count+=1
                    x+=1
                newans += str(count)+str(prev)
                count = 0
                if x < len(ans): 
                    prev = ans[x]
            ans = newans
            n-=1
        return ans