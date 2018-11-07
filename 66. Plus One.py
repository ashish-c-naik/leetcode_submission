class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        newarr = digits[::-1]
        flag = True
        for index,num in enumerate(newarr):
            if flag:
                num += 1
            if num > 9:
                num = 0
            else:
                newarr[index] = num
                flag = False
                break
            newarr[index] = num
        if flag:
            newarr.append(1)
        return newarr[::-1]
        