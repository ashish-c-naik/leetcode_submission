class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        self.d = {}
        def getorset(a):
            if a not in self.d:
                self.d[a] = a
                return self.d[a]
            elif self.d[a] == a:
                return self.d[a]
            else: return getorset(self.d[a])
        for a,o,_,b in equations:
            if o == '=': self.d[getorset(a)] = getorset(b)
        return not any(getorset(a) == getorset(b) for a,o,_,b in equations if o == '!')