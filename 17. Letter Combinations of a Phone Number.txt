class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        import itertools
        d = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        digit = []
        for x in digits:
             digit.append(d[x])
        ans = list(itertools.product(*digit))
        ans1 = []
        for x in ans:
            ans1.append(''.join(x))
        return (ans1)
        