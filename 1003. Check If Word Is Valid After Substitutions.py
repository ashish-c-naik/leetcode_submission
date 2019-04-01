class Solution(object):
    def isValid(self, S):
        """
        :type S: str
        :rtype: bool
        """
        d = {'a':0, 'b':0, 'c': 0}
        for val in S:
            if val == 'b':
                if d["a"] == 0:
                    return False
                else:
                    d["a"] -= 1
                    d["b"] += 1
            elif val == 'a':
                d['a'] += 1
            elif val == 'c':
                if d['b'] == 0:
                    return False
                else:
                    d['b'] -= 1
        if any(d[i]>0 for i in d.keys()): return False
        return True