class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        two = False
        nxt = False
        for x in range(len(bits)):
            if nxt:
                nxt = False
                continue
            if bits[x] == 1:
                two = True
                nxt = True
            else:
                two = False
        return not two
        