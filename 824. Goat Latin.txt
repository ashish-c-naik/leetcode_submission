class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowels = ['a','e','i','o','u']
        S = S.strip()
        l = S.split(" ")
        if not S:
            return ""
        ans = []
        for index,word in enumerate(l):
            index += 1
            ogword = word
            word = word.lower()
            if word[0] in vowels:
                ogword += 'ma'
            else:
                w = ogword[0]
                ogword = ogword[1:]
                ogword += w
                ogword += 'ma'
            ogword += 'a'*index
            ans.append(ogword)
        return " ".join(ans)