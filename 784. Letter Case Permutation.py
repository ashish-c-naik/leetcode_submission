class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        l = []
        def permute(s, l, ns):
            if ns =="":
                l.append(s)
            else:
                char = ns[0]
                ns = ns[1:]
                if char.isdigit():
                    permute(s+char, l, ns)
                else:
                    permute(s+char.lower(), l ,ns)
                    permute(s+char.upper(), l, ns)
        permute("", l, S)
        return (l)