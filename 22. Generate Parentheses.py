class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        def generate(left,right,str,ans):
            if left == right == 0:
                ans.append(str)
                return
            else:
                if left > 0:
                    generate(left-1,right,str+'(',ans)
                if right > left:
                    generate(left,right-1,str+')',ans)
        generate(n,n,"",ans)
        return ans