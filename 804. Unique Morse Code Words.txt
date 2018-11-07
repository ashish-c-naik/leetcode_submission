class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        l = []
        for x in words:
            symbol = ""
            for char in x:
                symbol += morse[ord(char) - ord('a')]
            l.append(symbol)
        return len(set(l))
                