class Solution(object):
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        The function recurses through different values of hours and minutes
        till it finds a time that fits.
        Note that for 'wx:yz' format
        -> w: takes values between (0,2)
        -> x: takes values between (0,9)
        -> y: takes values between (0,5)
        -> z: takes values between (0,9)
        and try to fit bigger number first in each index
        """
        string_one = ""
        string_two = ""
        def recurse(string, string1, count, A):
            if count == 4:
                if 0 <= int(string) < 24 and 0<= int(string1) < 60:
                    return True, string, string1, A
                else:
                    return False, string, string1, A
            else:
                if count == 0:
                    for x in range(2,-1,-1):
                        if x in A:
                            A.remove(x)
                            f, s, s1,  a = recurse(string+str(x), string1, count+1, A)
                            if f:
                                return  f, s, s1,  a
                            A.append(x)
                    return False, string, string1, A
                elif count == 1:
                    for x in range(9,-1,-1):
                        if x in A:
                            A.remove(x)
                            f, s, s1,  a= recurse(string+str(x), string1, count+1, A)
                            if f:
                                return  f, s, s1,  a
                            A.append(x)
                    return False, string, string1, A
                elif count == 2:
                    for x in range(5,-1,-1):
                        if x in A:
                            A.remove(x)
                            f, s, s1,  a = recurse(string, string1+str(x), count+1, A)
                            if f:
                                return  f, s, s1,  a
                            A.append(x)
                    return False, string, string1, A
                else:
                    for x in range(9,-1,-1):
                        if x in A:
                            A.remove(x)
                            f, s, s1,  a = recurse(string, string1+str(x), count+1, A)
                            if f:
                                return  f, s, s1,  a
                            A.append(x)
                    return False, string, string1, A
        f, string_one, string_two ,a = recurse("","", 0, A)
        if not f: return ""
        return (string_one +':'+ string_two)
                        