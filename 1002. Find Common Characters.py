class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        d = collections.Counter(A[0])
        d__ = {}
        for word in A[1:]:
            d_ = collections.Counter(word)
            for k in d_.keys():
                if k in d and k in d_:
                    d__[k] = min(d[k], d_[k])
            # print(d__)
            d = d__.copy()
            d__ = {}
        ans = []
        for k in d.keys():
            ans += [k]*d[k]
        return ans
                