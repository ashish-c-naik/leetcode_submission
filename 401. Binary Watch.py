class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        # if num == 0: return ["0:00"]
        def gettime(string):
            return int(string, 2)
        ans = []
        for x in range(num+1):
            string = ""
            for n in range(12):
                if bin(n)[2:].count("1") == x:
                    string += str(n)+":"
                    copy = string
                    for y in range(60):
                        if bin(y)[2:].count("1") == num-x:
                            string += str(y).zfill(2)
                            ans.append(string)
                        string = copy
                string = ""
        return ans