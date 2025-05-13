class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        first = strs[0]
        for i in strs[1:]:
            while i.find(first)!=0:
                first=first[:-1]

        return first
                
        