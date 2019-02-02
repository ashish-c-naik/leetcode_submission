class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def r(items_rem, list, curr_num, val):
            if items_rem == 0:
                if sum(list) == val: self.ans.append(l)
            else:
                for i in range(curr_num, 10):
                    if val >= items_rem*i:
                        r(items_rem-1, list+[i], i+1, val)
        self.ans = []
        r(k, [], 1, n)
        return self.ans