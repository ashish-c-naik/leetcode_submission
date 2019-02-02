class Solution(object):
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        s = ''
        lg = (A, B)[A < B]
        sm = (B, A)[A < B]
        lg_c = 'a' if lg == A else 'b'
        sm_c = 'b' if lg == A else 'a'
        d = lg // sm
        while lg > 0 and sm > 0 and lg != sm:
            for i in range(2):
                s += lg_c
                lg -= 1
            s += sm_c
            sm -= 1
        while lg > 0 or sm >0:
            if lg >0 :
                s += lg_c
                lg -= 1
            if sm > 0:
                s += sm_c
                sm -= 1
        if sm > 0: s += (sm_c * sm)
        if lg > 0: s += (lg_c * lg)

        return s
        
        
        
                