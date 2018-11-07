class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        pointer_1 = 0
        pointer_2 = 0
        while pointer_1 < len(name) and pointer_2 < len(typed):
            # FOR STRING 1: Count the occurances of the char
            count_1 = 0
            char_1 = name[pointer_1]
            while pointer_1 < len(name) and name[pointer_1] == char_1:
                count_1 += 1
                pointer_1 += 1
        
            # SAME FOR STRING 2
            count_2 = 0
            char_2 = typed[pointer_2]
            while pointer_2 < len(typed) and typed[pointer_2] == char_2:
                count_2 += 1
                pointer_2 += 1
                
            # INVALID STRING: Compare the occurances
            if count_1 > count_2:
                return False
        
        # If two pointers are at the end of respective strings return True
        return pointer_1 == len(name) and pointer_2 == len(typed)
            
        