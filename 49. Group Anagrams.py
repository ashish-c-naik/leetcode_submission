class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hash_table = collections.defaultdict(list)
        for str in strs:
            y = ''.join(sorted(str))
            hash_table[y].append(str)
        return (hash_table.values())