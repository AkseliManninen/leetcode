# Time Complexity: O(n * m)
# Space Complexity: O(1)

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if needle in haystack: 
            return haystack.index(needle) 
        else:
            return -1