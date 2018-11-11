class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        for x in S:
            if x=='(':
                stack.append(x)
            elif x==')':
                count = 0
                while stack and stack[-1]!='(':
                    count+=stack[-1]
                    stack = stack[:-1]
                if count > 0:
                    stack[-1] = 2*count
                else:
                    stack[-1] = 1
        return sum(stack)
            